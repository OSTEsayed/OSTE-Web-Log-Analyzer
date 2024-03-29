import argparse
import time
from datetime import datetime, timedelta

def start():
    global users,log_file_path
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split(' ')  # Assuming space-separated fields
            ip_address = parts[0]
            timestamp = parts[3][1:] #+ ' ' + parts[4][:-1]  # Combine date and time
            request_method = parts[5][1:]
            requested_uri = parts[6]
            status_code = parts[8]        
            user_agent = ' '.join(parts[11:])  # Join the user agent parts
            if ip_address in users:
                users[ip_address].append([timestamp,request_method,requested_uri,status_code,user_agent])
            else:
                users[ip_address]= [[timestamp,request_method,requested_uri,status_code,user_agent]]
#        print(f"IP: {ip_address}, Timestamp: {timestamp},Method: {request_method},URL: {requested_uri},Status: {status_code}, User Agent: {user_agent}")
    
    
#    for user in users.keys():
#       print(len(users[user]))

def group_dates_by_ratio(date_list, ratio_seconds=10, threshold_count=20):
  #  print(date_list[0][0])
 #   date_list[0][0]=datetime.strptime(date_list[0][0], '%d/%b/%Y:%H:%M:%S')
    date_groups = []
    current_group = [date_list[0][0]]
    count=0
    number=0
    for i in range(1, len(date_list)):
#        date_list[i][0]=datetime.strptime(date_list[i][0], '%d/%b/%Y:%H:%M:%S')    

        time_diff = (datetime.strptime(date_list[i][0], '%d/%b/%Y:%H:%M:%S')  - datetime.strptime(date_list[number][0], '%d/%b/%Y:%H:%M:%S') ).total_seconds()

        if time_diff <= ratio_seconds:
            current_group.append(date_list[i])
        else:
            number=i
            if len(current_group) >= threshold_count:
                date_groups.append(current_group)
            current_group = [date_list[i]]        
    # Check the last group
    if len(current_group) >= threshold_count:
            date_groups.append(current_group)

    return date_groups
def check_tools(data):
    file_path = 'Lib/Listoftools'
    name_list = []
    alert = {}
    with open(file_path, 'r') as file:
        for line in file:
            name = line.strip().lower()
            name_list.append(name)
    for sampl in data:
        for tool in name_list:
            if tool.lower() in sampl[4].lower():                
                if tool in alert.keys():
                   alert[tool][0]+=1
                   alert[tool][1].append(sampl)
                else:
                    alert[tool]= [1,[sampl]]
    return alert
def scan():
    global users,alerts
    for user in users.keys():
        
        #Checking For indication of automated tool By sending multiple request in small time rate (more than 20 in 10 sec):
        result_groups=group_dates_by_ratio(users[user])
        if len(result_groups)>0 :
            if user in alerts:
                alerts[user][0]+=len(result_groups)
                for group in result_groups:
                    alerts[user][1].append([f"Multiple Requests in small time rate(10s) (number of req:{len(group)})",len(group)])
            else:
                alerts[user]=[len(result_groups),[] ]            
                for group in result_groups:
                    alerts[user][1].append([f"Multiple Requests in small time rate(10s) (number of req:{len(group)})",len(group)])
        #checking for indication of the use of automated tools
        result_tools=check_tools(users[user])
#        print(result_tools)
        if len(result_tools.keys()) >0:
            for tool in result_tools:
#                print(tool)
                if user in alerts:
                    alerts[user][0]+=result_tools[tool][0]
                    alerts[user][1].append([f"Usage of automated scanning tool namely {tool}",len(result_tools[tool][1]),result_tools[tool][1]])                
                else:
                    alerts[user]=[result_tools[tool][0],[] ]            
                    alerts[user][1].append([f"Usage of automated scanning tool namely {tool}",len(result_tools[tool][1]),result_tools[tool][1]])                
        
def get_ips():
    global users
    print(users.keys())
    return users.keys()
  
def scan_ip(ip):
    print("scanne les request ta3o kol wyjib number dalerts, wfah metwswslo")
    return "Mazal"


def main():
    global log_file_path 
    log_file_path = 'LogSampls/access.log'
 

    global users,alerts 
    users = {}
    alerts = {}
    
    parser = argparse.ArgumentParser(description='WLA-cli -l exmpl.log [option] [value]')
    # Add the -l option
    parser.add_argument('-l', '--log', type=str, help='Specify the log path exampl: directoy/exampl.log')
    parser.add_argument('-t', '--total', action='store_true', help='perform a total Scan of the log')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the -l option is provided
    if args.log:
        log_file_path= args.log
        print(f'log file: {args.log}')
        if args.total:
            start()
            scan()
#            print(alerts)
            for user in alerts:
                for i in range(len(alerts[user][1])):
                    print (alerts[user][1][i][0])

    else:
        print('No log provided.')


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f'Total running time: {elapsed_time:.2f} seconds')
    
