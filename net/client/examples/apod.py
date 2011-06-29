import urllib as url
import re as re

def apod_baseurl():
    return "http://apod.nasa.gov/apod/"

def apod_url(month, day, year):
    datestr = "%02d%02d%02d" % ((year % 100), month, day)
    return "%sap%s.html" % (apod_baseurl(), datestr)

def get_apod_image_url(aurl):
    f = url.urlopen(aurl)
    for line in f:
        if re.search(r'[Ss][Rr][Cc]', line) is not None:
            return apod_baseurl()+re.split(r'^.*[Ss][Rs][Cc]=\"(.+)\".*', line)[1]
    f.close
    return None

if __name__ == '__main__':
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--server', dest='server', default='http://nova.astrometry.net/api/',
                      help='Set server base URL (eg, http://nova.astrometry.net/api/)')
    parser.add_option('--apikey', '-k', dest='apikey',
                      help='API key for Astrometry.net web service; if not given will check AN_API_KEY environment variable')
    opt,args = parser.parse_args()
    if opt.apikey is None:
        # try the environment
        opt.apikey = os.environ.get('AN_API_KEY', None)
    if opt.apikey is None:
        parser.print_help()
        print
        print 'You must either specify --apikey or set AN_API_KEY'
        sys.exit(-1)
    for year in range(1996, 2013):
        for month in range(1, 13):
            print "apod.py __main__: working on month %d-%02d" % (year, month)
            for day in range(1, 32):
                iurl = get_apod_image_url(apod_url(month, day, year))
                if True:
                    cmd = "python ../client.py --server %s --apikey %s --urlupload \"%s\"" % (opt.server, opt.apikey, iurl)
                    print cmd
                if False:
                    if iurl is None:
                        continue
                    args = {}
                    args['apiurl'] = opt.server
                    c = Client(**args)
                    c.login(opt.apikey)
                    c.url_upload(iurl)
                    print c.submission_images(1)