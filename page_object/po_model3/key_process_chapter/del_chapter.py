"""
删除章节的流程要包含创建章节
复用创建章节流程

"""
from time import sleep

from page_object.po_model3.KEY_VALUE import KEY_WORD_VALUE3
# from page_object.po_model3.KEY_VALUE.KEY_WORD_VALUE3 import CHAPTER_NAME
from page_object.po_model3.key_process_chapter.add_chapter import OperateChapter
from page_object.po_model3.key_word_class.key_operate_browser import KeyOperateBrowser


class DelChapter(KeyOperateBrowser):

    def del_chapter(self, title):
        # 复用章节新增流程
        operate_chapter = OperateChapter(self.driver)  # 继承类KeyOperateBrowser 的构造方法 构造方法里初始化了一个driver，这里需要初始化
        operate_chapter.chapter_add(title, KEY_WORD_VALUE3.TEST_CONTENT)
        sleep(2)
        # 定位新增的章节 章节名称
        # self.find_el(KEY_WORD_VALUE3.CREATE_CHAPTER_NAME,
        #              f"//tr[@class='book_list']//td[contains(text(),{title})]")
        # sleep(1)
        # 确认删除按钮
        self.find_el(*KEY_WORD_VALUE3.CHAPTER_DELETE).click()
        sleep(1)
        # 确认删除弹框按钮
        self.find_el(*KEY_WORD_VALUE3.ENSURE_BUTTON).click()
        sleep(2)
        # 新章节列表第一个章节的章节名
        first_chapter_name = self.find_el(*KEY_WORD_VALUE3.CHAPTER_LIST_FIREST).text
        return first_chapter_name
        # 校验放在test文件里
