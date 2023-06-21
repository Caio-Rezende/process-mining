import pandas
import pm4py

file_csv = './pm4py/assets/running-example.csv'
# file_xes = file_csv.replace('.csv', '.xes')
file_xes = './pm4py/assets/public/Sepsis_log.xes'
output_dir = './pm4py/outputs'


def import_csv(file_path):
    event_log = pandas.read_csv(file_path, sep=';')
    num_events = len(event_log)
    num_cases = len(event_log.case_id.unique())
    print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))
    return event_log


def analyze_start_end(event_log):
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(
        start_activities, end_activities))


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
    pm4py.save_vis_heuristics_net(
        heu_net, f'{output_dir}/ptree-inductive.png')
    pm4py.view_process_tree(process_tree)
    view_bpmn('inductive', process_tree)
    return process_tree


def heuristic(df):
    heu_net = pm4py.discover_heuristics_net(df)
    pm4py.save_vis_heuristics_net(
        heu_net, f'{output_dir}/net-heuristics.png')
    pm4py.view_heuristics_net(heu_net)
    return heu_net


def petri_heuristic(df):
    petri_net, im, fm = pm4py.discover_petri_net_heuristics(df)
    pm4py.save_vis_petri_net(
        petri_net, im, fm, f'{output_dir}/petri-heuristics.png')
    pm4py.view_petri_net(petri_net, im, fm)
    view_bpmn('heuristic', petri_net, im, fm)
    return petri_net, im, fm


def alpha(df):
    petri_net, im, fm = pm4py.discover_petri_net_alpha_plus(df)
    pm4py.save_vis_petri_net(
        petri_net, im, fm, f'{output_dir}/petri-alpha.png')
    pm4py.view_petri_net(petri_net, im, fm)
    view_bpmn('alpha', petri_net, im, fm)
    return petri_net, im, fm


def view_bpmn(title, *args):
    bpmn_model = pm4py.convert_to_bpmn(*args)
    pm4py.save_vis_bpmn(bpmn_model, f'{output_dir}/bpmn-{title}.png')
    pm4py.view_bpmn(bpmn_model)


if __name__ == "__main__":
    # df = get_df_from_csv()
    df = get_df_from_xes()
    analyze_start_end(df)
    # export_xes(df)
    # export_csv(df)
    heu_net = heuristic(df)
    process_tree = inductive(df)

    petrih_net, im, fm = petri_heuristic(df)
    petria_net, im, fm = alpha(df)
