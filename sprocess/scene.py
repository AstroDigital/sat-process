import re
import gippy
from errors import SatProcessError


class Scene(gippy.GeoImage):
    """ Collection of bands for the same scene """

    @property
    def bands(self):
        return self.bandnames()

    @property
    def band_numbers(self):
        return self.nbands()

    def get_bandname_from_file(self, value):

        # print(value)
        search = re.search('(B.{1,3})\.', value)
        if search:
            return search.group(0).replace('.', '')
        else:
            return None

    def select(self, *args, **kwargs):
        """ Return instance of Scene instead of GeoImage """
        img = super(Scene, self).select(*args, **kwargs)
        return self.__class__(img)

    def autoscale(self, *args, **kwargs):
        """ Return instance of Scene instead of GeoImage """
        img = super(Scene, self).autoscale(*args, **kwargs)
        return self.__class__(img)

    def has_bands(self, bands):
        for b in bands:
            if b not in self.bands:
                raise SatProcessError('Band %s is required' % b)