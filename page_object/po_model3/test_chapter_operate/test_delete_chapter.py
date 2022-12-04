from page_object.po_model3.KEY_VALUE.KEY_WORD_VALUE3 import TEST_TITLE
from page_object.po_model3.key_process_chapter.del_chapter import DelChapter


def test_delete_chapter(get_browser):
    del_chapter = DelChapter(get_browser)
    return_chapter_name = del_chapter.del_chapter(TEST_TITLE)
    assert return_chapter_name != TEST_TITLE
