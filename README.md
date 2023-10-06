Generate clips from a video file.



![clips_ss.jpg](assets%2Fclips_ss.jpg)

### Install dependencies

```
pip install -r requirements.txt
```

ImageMagick is required. 

If you are using Linux you must edit the policy.xml
/etc/ImageMagick-6/policy.xml comment out the line (its at the end):
```
<!-- <policy domain="path" rights="none" pattern="@*" /> -->
```

### Usage
Update the variables in config.toml and execute main.py