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

## Future Work
- Multi-signal digital downconversion
- Signal bandwidth and spectral analysis
- FM demodulation
- RTL-SDR-based reception and measurements

## Project Status
Ongoing learning and experimental development.
