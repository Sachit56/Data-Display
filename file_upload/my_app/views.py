from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import pandas as pd
import os


def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES['file']
        upload_instance = Upload.objects.create(upload=upload_file)

        file_path = upload_instance.upload.path


        df = pd.read_csv(file_path)

        if df.empty:
            return HttpResponse("The uploaded file is empty or improperly formatted.", status=400)

        required_columns = ['Date', 'Cust State', 'DPD', 'ACCNO', 'Cust Pin']
        if not all(column in df.columns for column in required_columns):
            return HttpResponse("CSV file is missing one or more required columns.", status=400)
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
   

        for i, row in df.iterrows():
            Datas.objects.create(
                date=row['Date'].strftime('%Y-%m-%d'),
                state=row['Cust State'],
                dpd=row['DPD'],
                account=row['ACCNO'],
                pin=row['Cust Pin']
            )

        return redirect('summary')

    return render(request, 'my_app/upload.html')
def summary(request):
    data = Datas.objects.all()
    return render(request,'my_app/summary.html',{'data':data})
