from assignment1.name_detector import censor_names
from assignment1.address_detector import censor_address
from assignment1.phone_detector import censor_phone
from assignment1.date_detector import censor_date
import warnings
warnings.filterwarnings("ignore")
def mask_content(file_content, stats):
    '''This function passes the file_content into different censoring pipelines and censors the detected entities'''
    file_content, stats = censor_names(file_content, stats)
    file_content, stats = censor_address(file_content, stats)
    file_content, stats = censor_phone(file_content, stats)
    file_content, stats = censor_date(file_content, stats)
    return file_content, stats

