# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/20 15:01
# @Author: Enbryan Xie
import datetime
import os.path
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from common.yaml_config import GetConf

from common.tools import get_project_path, get_img_path, sep

from common.find_img import FindImg

from common.report_add_img import add_img_2_report
from common.report_add_img import add_img_path_2_report

class ObjectMap:
    url = GetConf().get_utl()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        #  开始时间
        start_ms = time.time()*1000

        # 结束时间
        stop_ms = start_ms + (timeout*1000)

        for x in range (int(timeout*10)):
         # 查找元素
            try:
                element= driver.find_element(by=locate_type, value=locator_expression)
            # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素必须是可见的，则需要先判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception
            except Exception:
                now_ms=time.time()*1000
            if now_ms >= stop_ms:
                break

        raise ElementNotVisibleException(f"元素定位失败， 定位方式{locate_type}, 定位时间{now_ms}")
        # print(start_ms)



    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        判断页面是否加载完成
        """
        # 设置开始时间
        start_ms = time.time()
        # 结束时间
        stop_ms = start_ms + (timeout*1000)

        for x in range(int(timeout*10)):
            try:
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                sleep(0.03)
                return True
            # 如果页面完全加载完
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            # 页面没有完全加载完， 判断是否在设置时间范围内
            else:
                now_ms = time.time()*1000
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception ("打开网页时，页面元素在%s后仍然没有完全加载完"%timeout)

    def element_disappear(self, driver,locator_type, locator_expression, timeout=30):
        """
        等待页面元素消失
        """
        # 有元素定位方式
        if locator_type:
            # 设置开始和结束时间
            start_ms = time.time()
            stop_ms  = start_ms + (timeout*1000)

            for x in range (int(timeout*10)):
                try:
                    element = driver.find_element(by=locator_type, value=locator_expression)
                    if element.is_displayed:
                        now_ms =time.time()*1000
                        if now_ms >=  stop_ms:
                            break
                        else:
                            time.sleep(0.1)
                except Exception:
                    return  True
                raise Exception (f"元素没有消失，定位方式{locator_type}, 定位表达式{locator_expression}")
        else:
            pass

    def element_appear(self, driver, locator_type, locator_expression, timeout=30):
        """
        等待页面元素的出现
        """
        if locator_type:
            # 设置开始和结束时间
            start_ms=time.time()
            stop_ms = start_ms + (timeout*1000)

            for x in range(int(timeout*10)):
                try:
                    element = driver.find_element(by=locator_type, value=locator_expression)
                    if element.is_displayed:
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time()*1000
                    if now_ms >=stop_ms:
                        break
                    time.sleep(0.1)

            raise ElementNotVisibleException(f"元素没有出现，定位方式{locator_type}, 定位表达式{locator_expression}")
        else:
            pass
    def element_to_url(
            self,
            driver,
            url,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None
    ):
        try:
            """
            跳转地址
            """
            driver.get(self.url+url)
            #  等待页面加载完成
            self.wait_for_ready_state_complete(driver)

            # 跳转后等待元素消失
            self.element_disappear(driver,
                                   locate_type_disappear,
                                   locator_expression_disappear
                                   )

            # 跳转后等待元素出现
            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )
        except Exception as e:
            print("跳转地址出现异常，异常原因：%s" % e)
            return False

        return True

    def element_is_display(self,driver,locate_type, locator_expression):
        """
        元素是否显示
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False

    def element_fill_value(self,driver, locate_type, locator_expression, fill_value,timeout=30):
        """
        元素填值
        """
        # 元素必须先出现
        element=self.element_appear(
            driver,
            locator_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )

        try:
            # 先清除元素中的原有值
            element.clear()
        except StaleElementReferenceException: # 页面元素没有刷新出来，就对元素进行捕获，从而引发了这个异常
            self.wait_for_ready_state_complete(
                driver=driver
            )
            time.sleep(0.06)
            element = self.element_appear(
                driver,
                locator_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )

            try:
                element.clear()
            except Exception:
                pass

        except Exception:
            pass

        # 填入的值转成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)

        try:
            #填入的值不是\n结尾
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression)
            element.clear()
            if not fill_value.endswith(fill_value):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)

        except Exception:
            raise Exception("元素填值失败")

        return True

    def copy_element_fill_value(self, driver,locate_type, locator_expression,fill_value, timeout=30):
        # 元素必须先出现
        element = self.element_appear(driver=driver,
                            locate_type=locate_type,
                            locator_expression=locator_expression,
                            timeout=timeout)


        try:
            # 先清除元素中原有的值
            element.clear()
            # 这里有一个异常捕获
        except StaleElementReferenceException: # 页面元素未刷新出来，就对元素进行捕获，因此引发该异常
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.06)
            element = self.element_appear(
                driver=driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            try:
                element.clear()
            except Exception:
                pass

        except Exception:
            pass

        # 填入的值转成字符串
        if type (fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)

        try:
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                # 如果填入的值后面跟了\n， 就加一步回车操作
                fill_value=fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element=self.element_appear(
                driver=driver,
                locator_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            element.clear()
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)

            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)

        except Exception:
            raise Exception("元素填值失败")

        return True

    def element_click(
            self,
            driver,
            locate_type,
            locator_expression,
            wait_for_locate_type=None,
            wait_for_locator_expression=None,
            wait_for_disappear_locate_type=None,
            wait_for_disappear_locator_expression=None,
            timeout=30):
        """
        元素点击
        """
        # 元素必须可见
        element =self.element_appear(
            driver = driver,
            locator_type=locate_type,
            locator_expression=locator_expression,
            timeout=30
        )

        try:
            # 点击元素
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver,timeout=timeout)
            time.sleep(0.06)
            element = self.element_appear(
                driver=driver,
                locator_type=locate_type,
                locator_expression=locator_expression,
                timeout=30
            )
            element.click()
        except Exception as e:
            print("页面元素异常，元素不可点击",e)
            return False

        try:
            # 点击元素后的元素出现或元素消失
            self.element_appear(
                driver,
                wait_for_locate_type,
                wait_for_locator_expression,
                timeout=30
            )
            self.element_disappear(
                driver,
                wait_for_disappear_locate_type,
                wait_for_disappear_locator_expression,
                timeout=30
            )
        except Exception as e:
            print("等待元素出现或元素消失", e)
            return False
        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        文件上传
        """
        element = self.element_get(driver, locate_type, locator_expression )
        return element.send_keys (file_path)

    def switch_window_2_latest_handle(self, driver):
        """
        句柄切换窗口到最新的窗口
        """
        window_handles = driver.window_handles  # 获取所有窗口句柄
        driver.switch_to.window(window_handles[-1])  # 切换到最后一个（最新打开的）窗口


    def switch_into_iframe(self, driver, locate_iframe_type, locator_iframe_expression):

        """
        进入iframe
        """
        # 获取iframe
        iframe=self.element_get(driver, locate_iframe_type, locator_iframe_expression)

        # 进入iframe
        driver.switch_to.frame(iframe)

    def switch_from_iframe_to_content(self, driver):
        """
        从iframe切回主文档
        """
        driver.switch_to.parent_frame()

    def element_hover(self, driver, locate_type, locator_expression):
        """
        元素悬停
        """
        # 创建动作对象
        actions = ActionChains(driver)

        element_to_hover = self.element_get(driver, locate_type, locator_expression)

        actions.move_to_element(element_to_hover).perform()

    def find_img_in_source(self, driver, img_name):
        """
        截图并在截图中查找图片
        """
        # 截图后 图片保存的路径
        source_img_path = get_project_path() + sep(["img", "source_img", img_name], add_sep_before=True)
        # 需要查找的图片的路径
        search_img_path = get_project_path() + sep(["img", "assert_img", img_name], add_sep_before=True)

        # 截图并保存图片
        driver.get_screenshot_as_file(source_img_path)
        time.sleep(3)

        # 把我们的原图还有截图，都放入到测试报告中
        add_img_path_2_report(source_img_path, "原图")
        add_img_path_2_report(search_img_path, "需要查找的图片")

        # 在原图中查找是否有指定的图片， 返回信心值
        confidence = FindImg().get_confidence(source_img_path, search_img_path)

        return confidence

    def element_screenshot(self, driver, locate_type, locator_expression):

        """
        元素截图
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        # 先创建截图的文件名字
        ele_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"

        # 再创建并获取文件的保存路径
        ele_img_dir_path = get_project_path() + sep(["img", "ele_img"], add_sep_before=True, add_sep_after=True)

        # 如果文件夹不存在， 则进行创建
        if not os.path.exists(ele_img_dir_path):
            os.mkdir(ele_img_dir_path)

        # 拼接成一个完整的路径
        ele_img_path = ele_img_dir_path + ele_name

        # 对页面进行截图
        self.element_get(driver, locate_type, locator_expression).screenshot(ele_img_path)

        return ele_img_path
















































