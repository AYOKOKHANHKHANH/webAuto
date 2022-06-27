def get_chat_button_xpath():
    return "/html/body/div/div/div[1]/ul/a[1]"

def get_add_contact_button_id():
    return "channel-add-button"

def get_search_button_xpath():
    return "/html/body/div/div/div[2]/div[1]/div[1]/input"

def get_search_button_mini_xpath():
    return "/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/input"

def get_close_button_xpath():
    return "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button"

def get_inbox_button_xpath():
    return "/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/button"

def get_hello_start_button_css():
    # return "/html/body/div/div/div[2]/div[2]/div/div[3]/div"
    return ".w-full.mx-auto.relative .justify-center.font-semibold.cursor-pointer"

def get_hi_button_xpath():
    return "/html/body/div/div/div[2]/div[2]/div/div[2]/div/svg/path[2]"

def get_contact_in_list_friend_xpath():
    return "/html/body/div/div/div[2]/div[1]/div[3]"

def get_list_contact_button_id():
    return "appbar-contacts"

def get_wait_message_button_xpath():
    return "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[1]"

def get_agree_button_css():
    return ".flex.justify-end.space-x-1 .w-5.h-5.text-green-500"

def get_not_agree_button_css():
    return ".flex.justify-end.space-x-1 w-5 .h-5.text-red-primary"