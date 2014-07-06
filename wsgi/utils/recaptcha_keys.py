__author__ = 'adonis'


class RecaptchaKey():
    def __init__(self, request):
        host = request.get_host()
        if 'bovellcancerdiabetesfoundation.org' in host:
            self.host = 1
        elif 'bovellfoundation.org' in host:
            self.host = 2
        elif 'web-bcdf.rhcloud.com' in host:
            self.host = 3
        else:
            self.host = 0

    @property
    def public_key(self):
        if self.host == 1:
            return '6LdvXfYSAAAAAGaa5s5R56bs1xrDxm1LtUHJZ4cV'
        elif self.host == 2:
            return '6LcoO74SAAAAAD4lucDnw8LXQThIsmaOlp1o1MfK'
        elif self.host == 3:
            return '6Ld6UvYSAAAAAN_qwkhvWdKTyOOKJace6Kvk5bMo'
        else:
            return ''

    @property
    def private_key(self):
        if self.host == 1:
            return '6LdvXfYSAAAAAOZsVp-FUX9reQZyzvo3qaj-hLti'
        elif self.host == 2:
            return '6LcoO74SAAAAAE1c7qPU8Ohgwb6RhMt41JVIqgn9'
        elif self.host == 3:
            return '6Ld6UvYSAAAAAExqZ_LkDyVNgf3hxBK71Wgihbuq'
        else:
            return ''
