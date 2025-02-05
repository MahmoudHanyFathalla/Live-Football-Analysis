from ultralytics import YOLO 

model = YOLO('C:\\Users\\hp\\Desktop\\KoraState\\football_analysis-main\\football_analysis-main\\besttt.pt')

results = model.predict('C:\\Users\\hp\\Desktop\\KoraState\\football_analysis-main\\football_analysis-main\\08fd33_4.mp4',save=True)
print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)