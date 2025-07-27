# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/25 08:28
# @Author: Enbryan Xie

import aircv as ac
import cv2

from common.tools import get_project_path, get_img_path,sep, get_now_date_time_str

from common.report_add_img import add_img_2_report, add_img_path_2_report

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
        cv2.rectangle(img_src, results["rectangle"][0], results["rectangle"][3],
                      (255,0,0),2)
        diff_img_path = get_project_path() + sep(["img","diff_img", get_now_date_time_str()+".png"],
                                                 add_sep_before=True)
        cv2.imencode(".png", img_src)[1].tofile(diff_img_path)
        # add_img_2_report(diff_img_path,"查找到的图")

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
    source_path = get_project_path() + sep(["img", "source_img", "head_img.jpeg"], add_sep_before=True)
    search_path = get_project_path() + sep(["img", "assert_img","head_img.jpeg"], add_sep_before=True)
    FindImg().get_confidence(source_path, search_path)





