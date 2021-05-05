import math
import numpy as np

from feature_extraction.Feature import Feature
from feature_extraction.HRVFeaturesCalculator import HRVFeaturesCalculator


class KatzFeaturesCalculator(HRVFeaturesCalculator):
    """
    http://tux.uis.edu.co/geofractales/articulosinteres/PDF/waveform.pdf
    """

    def __init__(self, name, nni_signal):
        super().__init__(name, 'non-linear', nni_signal)

    def get_katz_fractal_dim(self):
        if not hasattr(self, 'katz_fractal_dim'):
            d_kfd = np.max([((1 - j) ** 2 + (self.nni[1] - self.nni[j]) ** 2) ** 0.5 for j in range(len(self.nni))])
            l_kfd = np.sum([(1 + (self.nni[i] - self.nni[i + 1]) ** 2) ** 0.5 for i in range(len(self.nni) - 1)])
            self.katz_fractal_dim = math.log10(l_kfd) / math.log10(d_kfd)
        return Feature(self.katz_fractal_dim, 'Katz fractal dimension')