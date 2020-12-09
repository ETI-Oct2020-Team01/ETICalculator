FROM python:3.7-slim
ADD notification.py /notification.py
RUN pip install --target=/app requests
RUN pip install twilio
RUN chmod +x /notification.py
CMD ["python", "/notification.py"]