import pm4py
import datetime as dt

file_xes='./pm4py/assets/running-example.xes'

def view(filtered):
    process_tree = pm4py.discover_process_tree_inductive(filtered)
    pm4py.view_process_tree(process_tree)

if __name__ == "__main__":
    log = pm4py.read_xes(file_xes)

    filtered = pm4py.filter_start_activities(log, {'register request'})
    view(filtered)
    
    filtered = pm4py.filter_start_activities(log, {'register request TYPO!'})
    view(filtered)

    filtered = pm4py.filter_end_activities(log, {'pay compensation'})
    view(filtered)

    filtered = pm4py.filter_event_attribute_values(log, 'resource', {'Pete', 'Mike'})
    view(filtered)

    filtered = pm4py.filter_event_attribute_values(log, 'resource', {'Pete', 'Mike'}, level='event')
    view(filtered)

    filtered = pm4py.filter_trace_attribute_values(log, 'concept:name', {'3', '4'})
    view(filtered)

    filtered = pm4py.filter_trace_attribute_values(log, 'concept:name', {'3', '4'}, retain=False)
    view(filtered)

    filtered = pm4py.filter_variants(log, [
        ['register request', 'check ticket', 'examine casually', 'decide', 'pay compensation']])
    view(filtered)

    filtered = pm4py.filter_variants(log, [
        ['register request', 'check ticket', 'examine casually', 'decide', 'reject request']])
    view(filtered)

    filtered = pm4py.filter_directly_follows_relation(log, [('check ticket', 'examine casually')])
    view(filtered)

    filtered = pm4py.filter_eventually_follows_relation(log, [('examine casually', 'reject request')])
    view(filtered)

    filtered = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31), mode='events')
    view(filtered)

    filtered = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31),
                                       mode='traces_contained')
    view(filtered)

    filtered = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31),
                                       mode='traces_intersecting')
    view(filtered)