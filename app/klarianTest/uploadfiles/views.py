from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.conf import settings

from uploadfiles.models import UploadedFile
from uploadfiles.models import ClientData

import csv
import json

# Create your views here.
# function to upload files with .json and .csv format
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get("file")
        print("uploaded_file")
        print(uploaded_file)
        print(str(uploaded_file))
        #print(uploaded_file.toString())
        if not uploaded_file:
            return HttpResponseBadRequest("No file uploaded or incorrect file field name")

        if not uploaded_file.name.endswith(('.json', '.csv')):
            return HttpResponseBadRequest("Only JSON or CSV files are allowed")

        file_obj = UploadedFile(file=uploaded_file)
        file_obj.save()
        print("FILE_OBJ")
        print(str(file_obj))
        #print(file_obj.toString())
        # Procesar el archivo y almacenar los datos en ClientData
        print(settings.UPLOADS_URL)
        file_url = str(settings.UPLOADS_URL) + str(file_obj)
        print("URL")
        print(file_url)
        if uploaded_file.name.endswith('.csv'):
            file_data = ""

            try:
                with open(file_url, newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    
                    for row in spamreader:
                        file_data = file_data + str(row)
                
                ClientData.objects.create(file=file_obj, data=file_data, type='TypeCSV')  # Ajusta el tipo según corresponda
                return JsonResponse({'message': 'File uploaded successfully!'})
            

            except FileNotFoundError as e:
                print(f"Error: File not found: {e}")
                return HttpResponseBadRequest(f"Error: File not found: {e}")

            except csv.Error as e:
                print(f"Error processing CSV file: {e}")
                return HttpResponseBadRequest(f"Error processing CSV file: {e}")

            except Exception as e:
                print(f"Other error: {e}")
                return HttpResponseBadRequest(f"Other error: {e}")

        
        elif uploaded_file.name.endswith('.json'):
            try:
                with open(file_url, 'r') as file:
                    data = json.load(file)
                print(data)  # Realiza alguna operación con los datos del archivo .json
                ClientData.objects.create(file=file_obj, data=json.dumps(data), type='TypeJSON')
                return JsonResponse({'message': 'File uploaded successfully!'})
                
            except FileNotFoundError as e:
                print(f"Error: File '{uploaded_file}' not found: {e}")
                return HttpResponseBadRequest(f"Error: File '{uploaded_file}' not found: {e}")

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON file: {e}")
                return HttpResponseBadRequest(f"Error decoding JSON file: {e}")

            except Exception as e:
                print(f"An error occurred: {e}")
                return HttpResponseBadRequest(f"An error occurred: {e}")
   
    return render(request, 'form_upload_file.html')


# funtion to manage query data
def query_data(request):
    data_type = request.GET.get('type')
    print("DATA TYPE")
    print(data_type)
    # fetch all data
    data = ClientData.objects.all().values()
    print("DATA")
    print(data)
    if data_type:
        # perform query filtering based on parameters
        data = data.filter(type=data_type)
    
    data_list = list(data.values())
    return JsonResponse(data_list, safe=False)