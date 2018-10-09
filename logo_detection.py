import os
import sys

import numpy as np

import cv2


def get_image(path):
    image = cv2.imread(path, 1)
    image_gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image, image_gry


def resize(image, x=0.5, y=0.5):
    return cv2.resize(image, (0, 0), fx=x, fy=y)


def parameter_tuning(name):
    bank = ''
    if name.find("BankOfAmerica") > -1:
        threshold = 0.5
        bank = 'Bank of America'
    elif name.find("CapitolOne") > -1:
        threshold = 0.9
        bank = 'Capitol One'
    elif name.find("Citigroup") > -1:
        threshold = 0.4
        bank = 'Citigroup'
    elif name.find("Chase") > -1:
        threshold = 0.5
        bank = 'Chase'
    elif name.find("WellsFargo") > -1:
        threshold = 0.5
        bank = 'Wells Fargo'
    else:
        threshold = 0.6
    return threshold, bank


def main():
    args = sys.argv
    filename = args[1]
    abs_path = os.path.dirname(os.path.abspath(__file__))
    template_folders = os.path.dirname(os.path.abspath(__file__)) + '/template'
    template_files = os.listdir(template_folders)

    image, image_gry = get_image(os.path.dirname(os.path.abspath(__file__)) +
                                 '/Images/' + filename)

    """
    cv2.imshow('file', file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
    found = False
    for template in template_files:
        if template.endswith('.png'):
            template_color, template_to_match = get_image(
                template_folders + '/' + template)
            """
            cv2.imshow('template_to_match', template_to_match)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            """
            if (image_gry.shape[0] <= template_to_match.shape[0] and template_to_match.shape[1] <= template_to_match.shape[1]):
                #methodss = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
                locations = []
                #method = eval(method)
                result = cv2.matchTemplate(
                    image_gry, template_to_match, cv2.TM_CCOEFF_NORMED)

                threshold, bank = parameter_tuning(template)

                locations = np.where(result >= threshold)
                if len(locations[::-1]) > 1:
                    #w, h, c = template_to_match.shape[::-1]
                    w, h = template_to_match.shape[::-1]

                    file_temp = cv2.imread(os.path.dirname(os.path.abspath(__file__)) +
                                           '/Images/' + filename)
                    found = False
                    for pt in zip(*locations[::-1]):
                        found = True
                        cv2.rectangle(
                            file_temp, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                        break
                    if found:
                        print(bank)
                        break
                        """
                        cv2.imwrite('res.png', file_temp)
                        result = cv2.imread(abs_path + '/res.png', 1)
                        #result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
                        cv2.imshow('cv2.TM_CCOEFF_NORMED', result)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        """
    if not found:
        print('Other')


if __name__ == '__main__':
    main()
