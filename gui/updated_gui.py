from tkinter import *
from PIL import ImageTk, Image
import datetime
from getdata import fetch_data_from_urls
import time

url1 = [
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SR/SR-AQ/SR-AQ-KH95-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WM/WM-WD/WM-WD-KH95-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-VN02-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WM/WM-WF/WM-WF-KB04-70/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-AQ/AQ-SN00-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-L001-03/Data/la",
    ]
url2 = [
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-VN03-00/Data/la",  
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-VN02-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-VN02-01/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-NI03-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-NI03-01/Data/la"
        ]
    
    


    # temp_label.config(text="" + f" {response_data[2]} \xb0C")
    # rh_label.config(text="" + f" {str(response_data[3][:-1])} %")
    # aqi_label.config(text="" + f" {response_data5[9]}")
    # signal_label.config(text="" + f" {response_data[1]} dB")
    # lux_label.config(text="NA" )
    # energy_label.config(text="" + f" {response_data3[1]} Kwh")
    # water_flow_label.config(text="" + f" {str(response_data4[2][:-1])}")
    # tds_label.config(text="" + f" {str(response_data1[4][:-1])}")
    # signal_label.config(text=""+f" {str(response_data6[2][2:-1])} dBm")
    # esg_co2_label.config(text=""+f"CO2 emission \n(saved)\n\n{(total)} kg")

    # esg_carbon_label.config(text=""+f"Carbon footprint \n(saved)\n\n{total/1000:.3f} tons")
    # # Update map
    # #map_widget.set_address("International Institute of Information Technology, Hyderabad")

   


root = Tk()
root.title("Sensor Data")
root.configure(background='#0A0A0A')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set geometry to full screen
root.geometry(f"{screen_width}x{screen_height}")

frame = Frame(root, bg='#0A0A0A')
frame.pack(pady=10)

# Create labels for time and day
time_label = Label(frame, text="Time: ", font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white')
time_label.pack(side=LEFT, anchor=NW, pady=(10, 5), padx=(30, 50))

day_label = Label(frame, text="Day: ", font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white')
day_label.pack(side=RIGHT, anchor=NW, pady=(10, 5), padx=(50, 30))

# Create a frame to contain the images
frame = Frame(root, bg='#0A0A0A')
frame.pack(pady=10)

# Load and resize the first image
image1 = Image.open(r"smartCity_livingLab.png").resize((150, 100))
photo1 = ImageTk.PhotoImage(image1)

# Load and resize the second image
image2 = Image.open(r"iiith_icon1.png").resize((150, 100))
photo2 = ImageTk.PhotoImage(image2)

# Create labels to display the images horizontally inside the frame
label1 = Label(frame, image=photo2, bg='#0A0A0A')
label1.image = photo1
label1.pack(side=LEFT, padx=(0, 20))  # Add padding on the right side of the first image

label2 = Label(frame, image=photo1, bg='#0A0A0A')
label2.image = photo2
label2.pack(side=LEFT, padx=(20, 0))  # Add padding on the left side of the second image

# Create a canvas for drawing the line below the frame
canvas_frame_line = Canvas(root, width=400, height=2, bg='#0A0A0A', highlightthickness=0)
canvas_frame_line.create_line(0, 0, 500, 0, fill="white", width=2)
canvas_frame_line.pack(pady=(5, 0))  # Adjust the padding to position the line below the frame

# Add a label for the text "Smart city dashboard"
label_text = Label(root, text="Smart City Dashboard", font=('Arial', 17, 'bold'), bg='#0A0A0A', fg='white')
label_text.pack(pady=(5, 0))  # Adjust the padding to position the label below the line


# Create a canvas for drawing the line below the text
canvas_text_line = Canvas(root, width=400, height=2, bg='#0A0A0A', highlightthickness=0)
canvas_text_line.create_line(0, 0, 500, 0, fill="white", width=2)
canvas_text_line.pack(pady=(5, 0))  # Adjust the padding to position the line below the text

image_frame = Frame(root, bg='#0A0A0A')
image_frame.pack(pady=10)

# Load and resize the image
image_path = r"nodes.png"  # Replace "path_to_your_image.jpg" with the actual path to your image
image = Image.open(image_path)
image = image.resize((400, 250))  # Adjust the size as needed
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = Label(image_frame, image=image, bg='#0A0A0A')
image_label.image = image  # Keep a reference to the image to prevent garbage collection
image_label.pack()

# Create a canvas for drawing the line below the text
canvas_text_line = Canvas(root, width=400, height=2, bg='#0A0A0A', highlightthickness=0)
canvas_text_line.create_line(0, 0, 500, 0, fill="white", width=2)
canvas_text_line.pack(pady=(2, 0))  # Adjust the padding to position the line below the text

label_text = Label(root, text="Lab Stats", font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
label_text.pack(pady=(2, 0))
# Create a canvas for drawing the line below the frame
canvas_frame_line = Canvas(root, width=400, height=2, bg='#0A0A0A', highlightthickness=0)
canvas_frame_line.create_line(0, 0, 500, 0, fill="white", width=2)
canvas_frame_line.pack(pady=(2, 0))  # Adjust the padding to position the line below the frame

# Create a frame for the sensor data columns
sensor_frame = Frame(root, bg='#0A0A0A')
sensor_frame.pack(pady=15)  # Increase the distance between the two columns

# Left column for sensor data
left_column = Frame(sensor_frame, bg='#0A0A0A')
left_column.pack(side=LEFT, padx=(10,40))  # Increase the padding for the left column

# Right column for sensor data
right_column = Frame(sensor_frame, bg='#0A0A0A')
right_column.pack(side=RIGHT, padx=(40,10))  # Increase the padding for the right column

# Load and resize the temperature icon
temp_icon = Image.open(r"temp_icon1.png").resize((30, 30))
temp_icon = ImageTk.PhotoImage(temp_icon)

# Add labels for sensor data
temp_label = Label(left_column, font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white', compound=LEFT, image=temp_icon)
temp_label.pack(anchor=W, pady=2)

rh_icon = Image.open(r"rh_icon.png").resize((30, 30))
rh_icon = ImageTk.PhotoImage(rh_icon)

rh_label = Label(left_column, font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white',compound=LEFT,image=rh_icon)
rh_label.pack(anchor=W, pady=2)

aqi_icon = Image.open(r"aqi_icon.png").resize((30, 30))
aqi_icon = ImageTk.PhotoImage(aqi_icon)

aqi_label = Label(left_column, font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white',compound=LEFT,image=aqi_icon)
aqi_label.pack(anchor=W, pady=2)

ss_icon = Image.open(r"ss_icon.png").resize((30, 30))
ss_icon = ImageTk.PhotoImage(ss_icon)

signal_label = Label(left_column, font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white',compound=LEFT,image=ss_icon)
signal_label.pack(anchor=W, pady=2)

lux_icon = Image.open(r"lux_icon.png").resize((30, 30))
lux_icon = ImageTk.PhotoImage(lux_icon)

lux_label = Label(right_column, font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white',compound=LEFT,image=lux_icon)
lux_label.pack(anchor=W, pady=2)

sl_icon = Image.open(r"sl_icon2.png").resize((30, 30))
sl_icon = ImageTk.PhotoImage(sl_icon)

energy_label = Label(right_column, font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white',compound=LEFT,image=sl_icon)
energy_label.pack(anchor=W, pady=2)

wf_icon = Image.open(r"wf_icon.png").resize((30, 30))
wf_icon = ImageTk.PhotoImage(wf_icon)

water_flow_label = Label(right_column, font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white',compound=LEFT,image=wf_icon)
water_flow_label.pack(anchor=W, pady=2)


wq_icon = Image.open(r"wq_icon.png").resize((30, 30))
wq_icon = ImageTk.PhotoImage(wq_icon)

tds_label = Label(right_column, font=('Arial', 13, 'bold'), bg='#0A0A0A', fg='white',compound=LEFT,image=wq_icon)
tds_label.pack(anchor=W, pady=2)

# Create a canvas for drawing the line below the text
canvas_text_line = Canvas(root, width=400, height=2, bg='#0A0A0A', highlightthickness=0)
canvas_text_line.create_line(0, 0, 500, 0, fill="white", width=2)
canvas_text_line.pack(pady=(1, 0))  # Adjust the padding to position the line below the text

label_text = Label(root, text="ESG Stats", font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
label_text.pack(pady=(2, 0))
# Create a canvas for drawing the line below the frame
canvas_frame_line = Canvas(root, width=400, height=2, bg='#0A0A0A', highlightthickness=0)
canvas_frame_line.create_line(0, 0, 500, 0, fill="white", width=2)
canvas_frame_line.pack(pady=(2, 0))  # Adjust the padding to position the line below the frame


# Create the main frame with a smaller width and height
esg_frame = Frame(root, bg='#0A0A0A', width=300, height=200)
esg_frame.pack(pady=15)  # Increase the distance between the two columns

# Left column for sensor data
esg_left_column = Frame(esg_frame, bg='#0A0A0A')
esg_left_column.pack(side=LEFT, padx=(10, 10))  # Increase the padding for the left column

# Right column for sensor data
esg_right_column = Frame(esg_frame, bg='#0A0A0A')
esg_right_column.pack(side=RIGHT, padx=(10, 10))

# Middle column for sensor data
esg_mid_column = Frame(esg_frame, bg='#0A0A0A')
esg_mid_column.pack(expand=True, fill=BOTH)  # Expand to fill the remaining space

# Add labels for sensor data
esg_co2_label = Label(esg_left_column,  font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
esg_co2_label.pack(anchor=W, pady=2)


esg_carbon_label = Label(esg_right_column,  font=('Arial', 10, 'bold'), bg='#0A0A0A', fg='white')
esg_carbon_label.pack(anchor=W, pady=2)


while True:

    time_label.config(text="Time: " + datetime.datetime.now().strftime("%H:%M"))
    day_label.config(text="Day: " +  datetime.datetime.now().strftime("%A"))
    try:
        data1, data2 = fetch_data_from_urls([url1, url2])
        print(data1)
        temp_label.config(text="" + f" {data1[0][0][1]} \xb0C")#
        rh_label.config(text="" + f" {str(data1[0][0][2][:-1])} %")#
        aqi_label.config(text="" + f" {str(data1[4][0])}")#
        lux_label.config(text="NA")
        energy_label.config(text="" + f"{data1[2][0]} Kwh")#
        water_flow_label.config(text="" + f" {str(data1[3][0][0:-1])}")
        tds_label.config(text="" + f" {str(data1[1][0][0:-1])}")
        d=(str(data1[5][0][2:5]))
        signal_label.config(text="" + f" {str(d)} dBm")##
    except IndexError:
        pass

    root.attributes('-fullscreen', True) 
    root.update()
    




