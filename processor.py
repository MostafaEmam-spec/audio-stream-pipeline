import os
import sys
import numpy as np

class StreamProcessor:
    def __init__(self, sample_rate=16000, channels=1):
        self.sample_rate = sample_rate
        self.channels = channels
        print(f"Initialized StreamProcessor at {sample_rate}Hz, Channels: {channels}")

    def normalize_audio(self, raw_bytes):
        data = np.frombuffer(raw_bytes, dtype=np.float32)
        peak = np.max(np.abs(data))
        if peak > 0:
            data = data / peak
        return data.tobytes()

if __name__ == "__main__":
    sp = StreamProcessor()
    print("Pipeline ready for ingestion.")
