# Camera

Before starting the server run:

```sh
python manage.py migrate
```

## Api Table
List of api's endpoints with params needed for these apis.

| Api Name                       | Param        | Description                                                    |
| ------------------------------ |:------------:|:---------------------------------------------------------------|
| `/modules/camera/photos/user/` | -No Params-  | Returns array of the images uploaded by the user. |
| `/modules/camera/upload_image/`|  object `{name, uri, type, data}`  |Gets object of image containing name, type uri and data about the image.             |


