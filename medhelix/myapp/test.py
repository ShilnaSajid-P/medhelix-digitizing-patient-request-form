def video_streaming(request):
    if request.method == 'POST':
        form = VideoStreamingForm(request.POST)
        if form.is_valid():
            # Convert the data URL into a byte array
            image_data = request.POST.get('image_data')
            image_data = image_data.replace('data:image/png;base64,', '')
            image_data = base64.b64decode(image_data)
            # Save the byte array as an image field
            video_streaming = VideoStreaming()
            video_streaming.image.save('image.png', ContentFile(image_data))
            video_streaming.save()
            return HttpResponse('Image captured and saved to database.')
    else:
        form = VideoStreamingForm()
    return render(request, 'index.html', {'form': form})

