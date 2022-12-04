from page_object.po_model2.key_process.chapter_process import ChapterProcess
from page_object.po_model2.key_word_list.KEY_WORD_VALUE2 import *


def test_add_chapter(get_browser):
    chapter_add = ChapterProcess(get_browser)
    chapter_add.login()
    chapter_add.chapter_add_process()
    chapter_new_object = chapter_add.find_el(*FIRST_CHAPTER)
    chapter_new_text = chapter_new_object.text()
    assert TEST_TITLE == chapter_new_text

