import pandas
import pm4py

file_csv='./pm4py/assets/running-example.csv'
file_xes=file_csv.replace('.csv', '.xes')

def import_csv(file_path):
    event_log = pandas.read_csv(file_path, sep=';')
    num_events = len(event_log)
    num_cases = len(event_log.case_id.unique())
    print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))
    return event_log

def analyze_start_end(event_log):
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

def export_xes(df):
    pm4py.write_xes(df, file_xes)

def export_csv(df):
    df.to_csv(file_csv.replace('.csv', '-exported.csv'))

def get_df_from_csv():
    event_log = import_csv(file_csv)
    return pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity', timestamp_key='timestamp', timest_format='%Y-%m-%d %H:%M:%S%z')

def get_df_from_xes():
    event_log = pm4py.read_xes(file_xes)
    return pm4py.convert_to_dataframe(event_log)

def inductive(df):
    process_tree = pm4py.discover_process_tree_inductive(df)
    pm4py.view_process_tree(process_tree)
    return process_tree

def heuristic(df):
    heu_net = pm4py.discover_heuristics_net(df)
    pm4py.view_heuristics_net(heu_net, format='svg')
    return heu_net

if __name__ == "__main__":
    #df = get_df_from_csv()    
    df = get_df_from_xes()    
    analyze_start_end(df)
    #export_xes(df)
    #export_csv(df)
    heu_net = heuristic(df)
    process_tree = inductive(df)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)