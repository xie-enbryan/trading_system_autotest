# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/25 08:28
# @Author: Enbryan Xie

import aircv as ac

from common.tools import get_project_path, get_img_path,sep

class FindImg:
    def img_imread(self, img_path):
        """
        读取图片
        """
        return ac.imread(img_path)


    # def get_confidence(self, source_path, search_path):
    #     """
    #     查找图片
    #     source_path： 原图路径
    #     search_path： 需要查找的图片的路径
    #     return
    #     """
    #     img_src = self.img_imread(source_path)
    #     img_sch = self.img_imread(search_path)
    #
    #     results = ac.find_template(img_src, img_sch)
    #
    #     print(results)
    #     confidence = float(results["confidence"])
    #     print(confidence)
    #     return confidence

    def get_confidence(self, source_path, search_path):
        """
        查找图片
        source_path： 原图路径
        search_path： 需要查找的图片的路径
        return
        """
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)

        # 执行图像匹配
        results = ac.find_template(img_src, img_sch)

        # 调试输出
        print(f"Results from image matching: {results}")

        # 检查结果是否为 None
        if results is None:
            raise ValueError(
                f"Image matching failed. Could not find confidence between {source_path} and {search_path}.")

        # 确保 results 有 "confidence" 键
        if "confidence" not in results:
            raise ValueError(f"Confidence not found in results: {results}")

        confidence = float(results["confidence"])
        return confidence


if __name__ == '__main__':
    source_path = get_project_path() + sep(["img", "个人头像1.jpeg"], add_sep_before=True)
    search_path = get_project_path() + sep(["img", "个人头像2.jpeg"], add_sep_before=True)
    FindImg().get_confidence(source_path, search_path)





