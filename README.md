Hello, my name is Brayn (it's supposed to be pronounced as Bryan) and this is just a vizualisation of:

1.) Raw Audio Input Digitalization - 
  The first graph represents the raw audio signal captured from the microphone of a guitar ( but any microphone really ) after 
it has been converted into digital data by the computer. When sound enters the microphone, physical air vibrations ( sound waves ) are
transformed into electrical signals and then sampled into discrete numerical values that can be processed by
the program. This graph displays how the audio amplitude changes over time, allowing the viewer to observe
the actual waveform of the sound being produced, such as guitar strings being played, claps, or speech. In
simple terms, this graph shows the direct digital representation of the sound before any mathematical
frequency analysis is performed.

2.) The Frequency Spectrum - 
  The second graph represents the frequency spectrum of the audio signal after it is processed 
using the Fast Fourier Transform (FFT) algorithm. While the first graph shows how sound amplitude changes over time, this
graph breaks the audio signal down into its individual frequency components. Each peak in the graph
represents a frequency that is present in the sound, with higher peaks indicating stronger energy at that
frequency. This visualization is useful for identifying the dominant frequency of a played note, which is used
to estimate pitch by locating the frequency with the highest magnitude energy within a valid human hearing
range. In simple terms, this graph shows the musical frequencies contained inside the sound and helps the
program approximate the pitch of the audio input.

--- it's a work in progress ---

I plan on adding first single pitch detection then chord detection using more Fourier transformations.
