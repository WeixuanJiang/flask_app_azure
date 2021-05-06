import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or 'se2_fsz2*fds1_pou0'
    
