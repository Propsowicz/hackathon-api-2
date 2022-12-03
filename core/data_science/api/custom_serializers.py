import json
from data_science.models import PlayerBio, Match, Season, DetailMatchStats
import pandas as pd
import numpy as np


def total_stats(season_id):
    matches = Match.objects.filter(season__id=season_id)
    total_stats = {
        'goals': 0,
        'assists': 0,
        'minutes': 0,
        'yellow_cards': 0,
        'red_cards': 0,
        'wins': 0,
        'draws': 0,
        'losts': 0,
        'team_goals_scored': 0,
        'team_goals_lost': 0,
        'team_goals_particip': 0,
        'clean_defence': 0

    }

    # todo:
    # goals/assist which made the final score of match
    # forma strzelecka

    matches_qty = matches.count()
    for _ in matches:
        total_stats['goals'] += _.player_goals
        total_stats['assists'] += _.player_assists
        total_stats['minutes'] += _.player_minutes
        total_stats['team_goals_scored'] += _.team_goals_scored
        total_stats['team_goals_lost'] += _.team_goals_lost      
        
        if _.player_yellow_card:
            total_stats['yellow_cards'] += 1
        if _.player_red_card:
            total_stats['red_cards'] += 1
        if _.team_goals_scored > _.team_goals_lost:
            total_stats['wins'] += 1
        elif _.team_goals_scored < _.team_goals_lost:
            total_stats['losts'] += 1
        else:
            total_stats['draws'] += 1
        if _.team_goals_lost == 0:
            total_stats['clean_defence'] += 1

    total_stats['goal_per_minutes'] = total_stats['minutes'] // total_stats['goals']
    total_stats['team_goals_particip'] = round(total_stats['goals'] / total_stats['team_goals_scored'] * 100, 1)

    spider_chart = []
    spider_chart.append({'team_goals_participation': total_stats['team_goals_particip']})
    spider_chart.append({'clean_defence_participation': round(total_stats['clean_defence'] / matches_qty * 100, 1) })
    spider_chart.append({'won_matches_ratio': round(total_stats['wins'] / matches_qty * 100, 1)})
    spider_chart.append({'lost_matches_ratio': round(total_stats['losts'] / matches_qty * 100, 1)})
    spider_chart.append({'total_minutes_ratio': round(total_stats['minutes'] / (matches_qty * 90) * 100, 1)})

    return [total_stats, spider_chart]

def each_match_stats(season_id):
    matches = Match.objects.filter(season__id=season_id)
    matches_details = DetailMatchStats.objects.select_related('match').filter(match__season__id=season_id)

    matches_stats = {
        'goals': [],
        'assists': [],
        'minutes': [],
        'yellow_cards': [],
        'red_cards': [],
        'tackles': [],
        'interceptions': [],
        'fouls': [],
        'blocks': [],
        'shots': [],
        'shots_on_target': [],
        'dribbled': [],
        'fouled': [],
        'offsides': [],
        'passes': [],
        'passes_on_target': [],
        'key_passes': [],
        'win': [],
        'draw': [],
        'lost': [],
    }

    for _ in matches_details:
        matches_stats['goals'].append(_.match.player_goals)
        matches_stats['assists'].append(_.match.player_assists)
        matches_stats['minutes'].append(_.match.player_minutes)
        matches_stats['tackles'].append(_.tackles)
        matches_stats['interceptions'].append(_.interceptions)
        matches_stats['fouls'].append(_.fouls)
        matches_stats['shots'].append(_.shots)
        matches_stats['shots_on_target'].append(_.shots_on_target)
        matches_stats['dribbled'].append(_.dribbles)
        matches_stats['fouled'].append(_.fouled)
        matches_stats['offsides'].append(_.offsides)
        matches_stats['passes'].append(_.passes)
        matches_stats['passes_on_target'].append(_.passes_on_target)
        matches_stats['key_passes'].append(_.key_passes)        
        
        if _.match.player_yellow_card:
            matches_stats['yellow_cards'].append(1)
        else:
            matches_stats['yellow_cards'].append(0)
        if _.match.player_red_card:
            matches_stats['red_cards'].append(1)
        else:
            matches_stats['red_cards'].append(0)
            
        if _.match.team_goals_scored > _.match.team_goals_lost:
            matches_stats['win'].append(1)    
            matches_stats['draw'].append(0)    
            matches_stats['lost'].append(0)    
        elif _.match.team_goals_scored < _.match.team_goals_lost:
            matches_stats['win'].append(0)    
            matches_stats['draw'].append(0)    
            matches_stats['lost'].append(1)    
        else:
            matches_stats['win'].append(0)    
            matches_stats['draw'].append(1)    
            matches_stats['lost'].append(0)     
        
    bar_chart = {
        'def':             
            {
                'tackles': sum(matches_stats['tackles']),
                'interceptions': sum(matches_stats['interceptions']),
                'fouls': sum(matches_stats['fouls']),
                'dribbled': sum(matches_stats['dribbled']),       
            },
        'attack':
            {
                'shots': sum(matches_stats['shots']),
                'shots_on_target': sum(matches_stats['shots_on_target']),
            },
        'pass':
            {   
                'passes': sum(matches_stats['passes']),
                'passes_on_target': sum(matches_stats['passes_on_target']),
                'key_passes': sum(matches_stats['key_passes'])
            }
    }

    perc_stats = {
        'def_success_rate': round((sum(matches_stats['tackles']) + sum(matches_stats['interceptions'])) / (sum(matches_stats['tackles']) + sum(matches_stats['interceptions']) + sum(matches_stats['fouls']) + sum(matches_stats['dribbled'])) * 100, 1),
        'att_success_rate': round(sum(matches_stats['shots_on_target']) / (sum(matches_stats['shots'])) * 100, 1),
        'pass_success_rate': round(sum(matches_stats['passes_on_target']) / (sum(matches_stats['passes'])) * 100, 1),
    }

    return matches_stats, bar_chart, perc_stats

def correlations(season_id):
    matches = Match.objects.filter(season__id=season_id)
    
    results = {
        'win': [],
        'draw': [],
        'lost': [],
    }
    
    minutes_corr = {
        'minutes': []        
        }
    goals_corr = {
        'goals': [],        
        }
    assists_corr = {
        'assists': [],
        }
    clean_corr = {
        'clean': [],
        }   

    for _ in matches:
        minutes_corr['minutes'].append(_.player_minutes)
        goals_corr['goals'].append(_.player_goals)
        assists_corr['assists'].append(_.player_assists)
        if _.team_goals_lost == 0:
            clean_corr['clean'].append(1)
        else:
            clean_corr['clean'].append(0)

        if _.team_goals_scored > _.team_goals_lost:
            results['win'].append(1)
        else:
            results['win'].append(0)
        if _.team_goals_scored < _.team_goals_lost:
            results['lost'].append(1)
        else:
            results['lost'].append(0)
        if _.team_goals_scored == _.team_goals_lost:
            results['draw'].append(1)
        else:
            results['draw'].append(0)

    minutes_corr = {**minutes_corr, **results}
    goals_corr = {**goals_corr, **results}
    assists_corr = {**assists_corr, **results}
    clean_corr = {**clean_corr, **results}   
    
    return [[pearson_corr(minutes_corr), pearson_corr(goals_corr), pearson_corr(assists_corr), pearson_corr(clean_corr)]]

def pearson_corr(data_dict):
    df = pd.DataFrame.from_dict(data_dict)
    Pcorr = df.corr()

    i = 0
    matrix_list = []
    for y_scale in Pcorr:
        matrix_list.append({y_scale: []})
        for x_scale, val in zip(Pcorr, np.array(Pcorr)[i]):                            
            if np.isnan(val):
                matrix_list[i][y_scale].append({'x': x_scale, 'y':0})
            else:
                matrix_list[i][y_scale].append({'x': x_scale, 'y':val})
        i += 1
    return matrix_list[0]

