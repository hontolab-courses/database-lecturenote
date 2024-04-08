import os
import pandas as pd



if not os.path.isfile('data/SSDSE.db'):
    os.makedirs('data', exist_ok=True)

    # ------------------
    # For SQL Day 1
    # ------------------
    target_columns_E = ['地域コード', '都道府県',  '調査年度', '総人口',
                      '小学校児童数', '中学校生徒数', '高等学校生徒数', '大学学生数']

    df_SSDSE_E_2021 = pd.read_csv(
        'https://www.nstac.go.jp/sys/files/SSDSE-E-2023.csv',
        encoding = "shift-jis", skiprows=2
    ).assign(
        調査年度=2021
    )[1:]

    df_SSDSE_E_2020 = pd.read_csv(
        'https://www.nstac.go.jp/sys/files/SSDSE-E-2022v2.csv',
        encoding = "shift-jis", skiprows=2
    ).assign(
        調査年度=2020
    )[1:]

    df_SSDSE_E = pd.concat([df_SSDSE_E_2021, df_SSDSE_E_2020])
    df_SSDSE_E[target_columns_E].to_sql(name='population',
                                        con='sqlite:///data/SSDSE.db',
                                        if_exists='replace', index=False)


    # ------------------
    # For SQL Day 2 & 3
    # ------------------
    df_SSDSE_E_2021 = pd.read_csv(
        'https://www.nstac.go.jp/sys/files/SSDSE-E-2023.csv',
        encoding = "shift-jis", skiprows=2
    )[1:]

    df_SSDSE_E_2021.sort_values(
        '65歳以上人口', ascending=False)[:10][['地域コード', '都道府県', '総人口']].to_sql(
        name='elderly_population_top10',
        con='sqlite:///data/SSDSE.db',
        if_exists='replace', index=False)

    df_SSDSE_E_2021.sort_values(
        '大学学生数', ascending=False)[:10][['地域コード', '都道府県', '総人口']].to_sql(
        name='university_student_population_top10',
        con='sqlite:///data/SSDSE.db',
        if_exists='replace', index=False)


    target_columns_D = ['地域コード', '都道府県', '学習・自己啓発・訓練の総数', 'スポーツの総数',
                      '趣味・娯楽の総数', 'ボランティア活動の総数', '旅行・行楽の総数']
    df_SSDSE_D = pd.read_csv(
        'https://www.nstac.go.jp/sys/files/SSDSE-D-2023.csv',
        encoding = "shift-jis", skiprows=1
    )[1:48][target_columns_D].rename(
        columns={'学習・自己啓発・訓練の総数': '学習・自己啓発・訓練',
                'スポーツの総数': 'スポーツ',
                '趣味・娯楽の総数': '趣味娯楽',
                'ボランティア活動の総数': 'ボランティア',
                '旅行・行楽の総数': '旅行・行楽'}
    ).pipe(
        lambda df: df[df.都道府県 != '京都府']
    ).to_sql(
        name='activity', con='sqlite:///data/SSDSE.db', if_exists='replace', index=False)
