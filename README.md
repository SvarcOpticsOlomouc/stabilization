# Sub-0.1 degree phase locking of a single-photon interferometer
Datasets and codes used in a scientific article xxx. Datasets are in .npy format with the filename "FigXcolor". Here "X" corresponds to the Fig indication (for example 4c), and "color" corresponds to the color plotted in the manuscript. The clue is following:

"Orange" - signal data
"Red" - reference data
"Black" - phase drift compensated (is equal to a drift of non-stabilized interferometer)

Further follows the specification of the format of each dataset:

Fig4
datasets are in format [time (s), data]

data = phase (degrees) for Fig4a
data = normalized spectral power density () for Fig4b
data = Allan deviation (degrees) for Fig4c

Fig5

datasets formats:
"data_Fig5a.npy" is in format [time (s), transmittance, reflectance]
"data_Fig5b.npy" is in format [time (min), transmittance, reflectance]

"data_Fig5a.npy" describes full tunability on continuously detected signal
"data_Fig5b.npy" describes full tunability on single-photon signal
