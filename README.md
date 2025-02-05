# Football Analysis Project

## Overview
This project focuses on leveraging advanced computer vision techniques to analyze football matches by detecting and tracking players, referees, and footballs within a video stream. The primary goal is to enhance the understanding of team dynamics and player movement throughout the match. YOLO, a state-of-the-art object detection model, is utilized for identifying and tracking key elements within the game. 

Furthermore, the project integrates several advanced techniques such as pixel segmentation, optical flow analysis, and perspective transformation to improve the accuracy and depth of the analysis. Player team identification is accomplished through clustering based on t-shirt color, while camera movement and player movement are measured using optical flow and perspective transformation, respectively. This comprehensive approach also allows for calculating player speeds and distances covered during the match.

## Features and Functionality
- **Player, Referee, and Ball Detection**: YOLO v5 is used for real-time object detection to identify players, referees, and footballs within each frame of the video.
  
- **Team Assignment**: Players are grouped into teams based on the color of their t-shirts. This is achieved through pixel segmentation and clustering using the K-means algorithm.

- **Ball Acquisition Percentage**: The project calculates the percentage of ball possession for each team by analyzing ball tracking data.

- **Player Movement Tracking**: Optical flow techniques are applied to track the movement of players and the ball across video frames, accounting for camera movement.

- **Perspective Transformation**: To account for depth and perspective in the scene, a transformation is applied to measure player movements in meters rather than pixels, offering a more accurate representation of movement within the physical world.

- **Speed and Distance Calculation**: The project calculates the speed and total distance covered by each player during the match, providing valuable insights into player performance.

## Modules and Libraries Used
The following modules and libraries are integral to the functioning of the project:

- **YOLO**: Utilized for AI-based object detection to identify players, referees, and footballs.
- **K-means**: A clustering algorithm used for t-shirt color segmentation and team assignment.
- **Optical Flow**: Analyzes camera movement and player motion across frames.
- **Perspective Transformation**: Calculates the real-world distances and movement from the video frames.
- **Additional Libraries**: 
  - OpenCV for video processing and computer vision tasks.
  - NumPy for numerical operations.
  - Matplotlib for visualization.
  - Pandas for data handling and analysis.

## Trained Models
The project employs the following pre-trained models:

- [Trained YOLO v5 Model](https://drive.google.com/file/d/1DC2kCygbBWUKheQ_9cFziCsYVSRw6axK/view?usp=sharing)

## Sample Video
To understand the application of the project, refer to the following sample video:

- [Sample Input Video](https://drive.google.com/file/d/1t6agoqggZKx6thamUuPAIdN_1zR9v9S_/view?usp=sharing)

## Requirements
Ensure the following software and libraries are installed to run the project:

- Python 3.x
- ultralytics (for YOLO model)
- supervision (for object tracking)
- OpenCV (for video and image processing)
- NumPy (for numerical operations)
- Matplotlib (for plotting and visualization)
- Pandas (for data manipulation and analysis)

This project provides valuable insights into the application of AI and computer vision in sports analytics, specifically in football match analysis. It is suitable for both beginners and experienced developers interested in exploring machine learning and computer vision techniques.
