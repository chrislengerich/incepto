# incepto
All code for the Incepto camera project goes here

## Image Server:
Displays the most recent image POSTed to it.

### Use:
#### Upload an image from disk:

* Curl: 

```
> curl -F "image=@/Users/thor/Downloads/totoro.jpg"  http://35.231.112.69/image?key=b09c4de1043f8ad0815d
```

* Python:

```
export API_KEY=b09c4de1043f8ad0815d
python client.py /Users/thor/Downloads/totoro.jpg
```

#### View images: 
http://35.231.112.69?key=b09c4de1043f8ad0815d
