# SDR and GNU Radio Receiver Experiments

## Overview
This repository documents my hands-on learning and experiments with Software Defined Radio (SDR) using GNU Radio Companion.

The project focuses on digital signal processing techniques used in communication receivers, including frequency conversion, filtering, and signal analysis.

## Tools
- GNU Radio Companion
- Python
- QT GUI Frequency Sink
- Complex signal sources and FIR filters

## Experiment 1: Digital Downconversion

**Objective:** Demonstrate frequency shifting using complex multiplication and signal selection using a low-pass filter.

### Flowgraph

Two complex signal sources are connected to a Multiply block, followed by a Low Pass Filter and QT GUI Frequency Sink.

### Configuration
- Sample rate: 32 kS/s
- Input signal frequency: +5 kHz
- Local oscillator: −5 kHz or −3 kHz
- Low-pass filter cutoff: 1 kHz
- Transition width: 500 Hz
- Filter window: Hamming

### Experimental Results

| Test | Output Frequency | Measured Spectrum Level |
|---|---|---|
| Mixer output without LPF (LO = −3 kHz) | +2 kHz | −9.5 dB |
| Mixer output with LPF (LO = −3 kHz) | +2 kHz | −68 dB |
| Mixer output with LPF (LO = −5 kHz) | 0 Hz | −7.02 dB |

The low-pass filter suppressed the +2 kHz spectral peak by approximately **58.5 dB**, based on measurements with the QT GUI Frequency Sink.

These values are relative spectral measurements, not calibrated RF power readings.

## Key Learnings
- Complex multiplication shifts signal frequencies.
- A digital mixer can move a selected signal to baseband.
- Low-pass filtering can suppress signals outside the desired passband.
- Digital downconversion is a fundamental operation in SDR receivers.

## Experiment 2: Multi-Signal Receiver and Channel Selection

### Objective
Simulate the reception of three complex signals and select one desired signal using digital downconversion and low-pass filtering.

### GNU Radio Flowgraph
Three complex Signal Source blocks are combined using an Add block. The combined signal is multiplied by a complex local oscillator and passed through a Low Pass Filter before spectral analysis.

**Signal processing chain:**

`3 Signal Sources → Add → Multiply (LO) → Low Pass Filter → QT GUI Frequency Sink`

### Configuration
- Sample rate: 32 kS/s
- Wanted signal: +5 kHz
- Unwanted signals: +1 kHz and +9 kHz
- Local oscillator: −5 kHz
- Low-pass filter cutoff: 1 kHz
- Transition width: 500 Hz
- Filter window: Hamming

### Experimental Results

| Input Signal | Frequency After Mixing | Measured Spectrum Level | Result |
|---|---|---|---|
| +1 kHz | −4 kHz | −80.12 dB | Suppressed |
| +5 kHz | 0 kHz | −8.2 dB | Passed |
| +9 kHz | +4 kHz | −80.12 dB | Suppressed |

### Analysis

The complex mixer shifted the desired +5 kHz signal to 0 Hz while shifting the two unwanted signals to −4 kHz and +4 kHz.

The low-pass filter preserved the desired signal near 0 Hz and strongly suppressed the unwanted signals.

The measured separation between the wanted peak and each unwanted peak was:

**−8.2 − (−80.12) = 71.92 dB**

This is a relative spectral peak separation measured using the GNU Radio QT GUI Frequency Sink, not a calibrated receiver rejection measurement.

### Key Learnings
- Combining multiple complex signals to simulate simultaneous reception
- Digital frequency shifting using a complex local oscillator
- Channel selection using a low-pass filter
- Spectral analysis and measurement of unwanted-signal suppression

### Experimental Flowgraph and Output
![Multi-Signal Receiver Flowgraph and Spectrum](multi_signal_receiver_result.png.png)


## Experiment 3: Amplitude Modulation (AM)

### Objective
To implement a conventional AM transmitter in GNU Radio and analyze the modulated signal in the time and frequency domains.

### GNU Radio Implementation
The AM transmitter was developed using:
- Two Signal Source blocks (Float)
- Add Const block
- Multiply block
- QT GUI Time Sink
- QT GUI Frequency Sink

### Simulation Parameters
| Parameter | Value |
|---|---|
| Sampling rate | 32 kS/s |
| Carrier frequency | 5 kHz |
| Message frequency | 200 Hz |
| Message amplitude | 0.5 |
| Carrier amplitude | 1 |
| DC offset | 1 |
| Modulation index | 50% |

### AM Signal Equation

`s(t) = [1 + 0.5 cos(2π × 200t)] cos(2π × 5000t)`

### Experimental Results
**Time Domain:** The carrier oscillates at 5 kHz while its amplitude envelope follows the 200 Hz message. The envelope magnitude varies between 0.5 and 1.5.

**Frequency Domain:** Three positive-frequency components were observed:

| Component | Frequency |
|---|---|
| Lower sideband (LSB) | 4.8 kHz |
| Carrier | 5.0 kHz |
| Upper sideband (USB) | 5.2 kHz |

Corresponding negative-frequency components appear because the AM signal is real-valued.

### AM Waveform and Frequency Spectrum

![AM Waveform and Frequency Spectrum](am_modulation_result.png.png)

### Key Learnings
- Generated a conventional AM signal using GNU Radio.
- Observed the message envelope in the time domain.
- Identified the carrier and two sidebands in the frequency spectrum.
- Understood the relationship between message frequency and sideband spacing.
- Learned how the modulation index affects the amplitude envelope.

### Next Step
Implement AM demodulation to recover the original message signal.

## Future Work
- Multi-signal digital downconversion
- Signal bandwidth and spectral analysis
- FM demodulation
- RTL-SDR-based reception and measurements

## Project Status
Ongoing learning and experimental development.
