# Postmortem

![https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Fsoftware-engineering-debugging-vector-line-icon-illustration-gm1089093136-292156402&psig=AOvVaw19a0_gH9LMegJSygFnc_Gv&ust=1710110384824000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCICqpeef6IQDFQAAAAAdAAAAABAD](https://media.istockphoto.com/id/1089093136/vector/software-engineering-debugging-vector-line-icon-illustration.jpg?s=2048x2048&w=is&k=20&c=QCaS-nx5CTJRQnjfQYI8_kAJN1vy8aFbFHz2Hjkd77s=)

## Summary
    - Pytube Youtube downloader issue
    - Detected 15.01.2022 Solved 20.01.2022    
    - Service Was Down
    - Cause Invalid Url request

## Timeline
### 15.01.2022 - Detecting the issue
### 16.01.2022 - The system was checked to figure out the problem
### 17.01.2022 - The misleading path was they took
### 19.01.2022 - The system was not as good as it was
### 20.01.2022 - The issue solved

## Root cause
    - The root cause of the problem was making request to url is not exists It happened because the user inserted resolution maybe is not available
    - The issue solved when we implemented a new function takes an argument it was the user desired resolution and trying to query if it exist or the return NONE

## Corrective and preventative measures
    - In Future we can implement a way that user choose between three things (Highest resolution, Lowest resolution, Custom resolution)
