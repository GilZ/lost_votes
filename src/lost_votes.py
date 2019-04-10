import pandas as pd
import data_customizers

customizer = data_customizers.DataCustomizer2019()


def run():
    df = pd.read_csv(customizer.get_file_path(), index_col=0, engine='python', encoding='iso8859_8')
    missing_ratio = df[customizer.col_name('potential_voters')] / df[customizer.col_name('legal_voters')]
    potential_df = df.iloc[:, customizer.first_party_ix:].multiply(missing_ratio, axis='index')
    actual_mandates = compute_mandates(df.iloc[:, customizer.first_party_ix:], df[customizer.col_name('legal_voters')])
    potential_mandates = compute_mandates(potential_df, df[customizer.col_name('potential_voters')])
    diff_df = pd.concat([actual_mandates, potential_mandates], axis=1)
    diff_df.columns = ['actual', 'potential']
    diff_df['diff'] = potential_mandates - actual_mandates
    diff_df.sort_values('diff', ascending=False, inplace=True)
    diff_df.rename(index=customizer.party_names, inplace=True)
    print(diff_df.to_csv())


def compute_mandates(df, count_col):
    total_per_party = df.sum()
    total_relevant_voters = count_col.sum()
    relevant = total_per_party[total_per_party / total_relevant_voters >= customizer.threshold]
    votes_per_mandate = relevant.sum() / 120
    mandates = relevant // votes_per_mandate
    spare_mandates = int(120 - mandates.sum())
    parties = pd.concat([mandates, relevant / (mandates + 1), relevant], axis=1)
    parties.columns = ['mandates', 'party_ix', 'votes']
    for _ in range(spare_mandates):
        getting_bonus = parties[parties['party_ix'] == parties['party_ix'].max()]
        getting_bonus['mandates'] += 1
        getting_bonus['party_ix'] = getting_bonus['votes'] / getting_bonus['mandates'] + 1
        parties.update(getting_bonus)
    return parties['mandates'].astype(int)


if __name__ == '__main__':
    run()
