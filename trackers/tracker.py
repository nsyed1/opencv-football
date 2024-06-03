from ultralytics import YOLO
import supervision as sv

class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def detect_frames(self, frames):
        batch_size = 20  # to prevent memory issues, 20 records are fed into model at one time
        detections = []
        # iterate over # of frames, increment by batch size
        for i in range(0, len(frames), batch_size):  
            detections_batch = self.model.predict(frames[i:i+batch_size], conf=0.1)
            detections += detections_batch
            break
        return detections

    def get_object_tracks(self, frames):
        detections = self.detect_frames(frames)

        # convert goalkeepers from person to goalkeeper
        for frame_num, detection in enumerate(detections):
            cls_names = detection.names
            cls_names_inv = {v:k for k,v in cls_names.items()}

            # convert to supervision detection format
            detection_supervision = sv.Detections.from_ultralytics(detection)

            print(detection_supervision)