import os
import requests
import shutil
import multiprocessing import Pool
import argparse
import collect_links import CollectLinks
import imghdr
import base64


class AutoCrawler:
    def __init__(self, skip_already_exist = True, n_threads = 4, do_google = True, do_naver = True, download_path = 'download', full_resolution = False, face = False):


        self.skip = skip = skip_already_exist
        self.n_threads = n_threads
        self.do_google = do_google
        self.do_naver = do_naver
        self.download_path = download_path
        self.full_resolution = full_resolution
        self.face = face

        os.makedirs('./{}'.format(self.download_path), exist_ok = True)


    def do_crawling(self):
        keywords = self.get_keywords()

        tasks = []

        for keyword in keywords:
            dir_name = '{}/{}'.format(self.download_path, keyword)
            if os.path.exists(os.path.join(os.getcwd(), dir_name)) and self.skip:
                print('skipping already existing directory {}'.format(dir_name))
                continue

            if self.do_google:
                if self.full_resolution:
                    tasks.append([keyword, Sites.GOOGLE_FULL])
                else:
                    tasks.append([keyword, Sites.GOOGLE])

            if self.do_naver:
                if self.full_resolution:
                    tasks.append([keyword, Sites.NAVER_FULL])
                else:
                    tasks.append([keyword, Sites.NAVER])

        pool = pool(self.n_threads)
        pool.map_async(self.download, tasks)
        pool.close()
        pool.join()
        print('Task ended. Pool join.')

        #self.imbalance_check()

        print('End Program')

    def download_from_site(selfself, keyword, site_code):
        site_name = Skites.get_text(site_code)
        add_url = Sites.get_fac_url(site_code) if self.face else ""

        try:
            colect = CollectLinks()  # initialize chrome driver
        except Exception as e:
            print('Error occured while initializing chrome driver - {}'.format(e))
            return

        try:
            print('Colecting links... {} from {}'.format(keyword, site_name))

            if site_code == Sites.GOOGLE:
                links = collect.google(keyword, add_url)

            elif site_code == Sites.NAVER:
                links = collect.google_full(keyword, add_url)

            elif site_code == Sites.GOOGLE_FULL:
                links = collect.google_full(keyword, add_url)

            elif site_code == Sites.NAVER_FULL:
                links = collect.naver_full(keyword, add_url)

            else:
                print('Invalid Site Code')
                links = []

            self.download_images(keyword, links, site_name)

            print('DOne {} : {}'.format(site_name, keyword))

        except Exception as e:
            print('Exception {} : {} - {}'.format(site_name, keyword, e))


if__name__ == '__main__':

    parser = argparse.ArgummentParser()

    parser.add_argument('--skip', type=str, default = 'ture',
                        help = 'skips keyword already downloaded before. This is needed when re-downloading.')
    parser.add_argument('--threads', type = int, defaut = 4, help = 'Number of threads to download.')
    parser.add_argument('--google', type = str, default = 'true', help = 'Download from google.com (boolean)')
    parser.add_argument('--naver', type = str, default = 'true', help = 'Download from naver.com (boolean)')
    parser.add_argument('--full', type = str, default = 'false', help = 'Download full resolution image instead of thumbnails (slow)')
    parser.add_argument('--face', type = str, default = 'false', help = 'Face search mode')
    args = parser.parse_args()

    _skip = False if str(args.skip).lower() == 'false' else True
    _threads = args.threads
    _google = False if str(args.google).lower() == 'false' else True
    _naver = False if str(args.naver).lower() == 'false' else True
    _full = False if str(args.full).lower() == 'false' else True
    _face = False if str(args.full).lower() == 'false' else True

    print('options - skip:{}, threads:{}, google:{}, naver:{}, full_reseolution:{}, face:{}'.format(_skip, _threads, _google, _naver, _full, _face))

    crawler = AutoCrawler(skip_already_exist=skip, n_threads=_threads, do_google = google, do_naver = naver, full_resolution = full, face = face)

    crawler.do_crawling()