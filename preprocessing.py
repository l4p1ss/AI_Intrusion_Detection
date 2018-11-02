import pandas as pd


def map2major5(df):
    d = {
        # NORMAL ATTACK
        'normal.': 0,

        # DOS ATTACK
        'apache2.': 1,
        'back.': 1,
        'mailbomb.': 1,
        'neptune.': 1,
        'pod.': 1,
        'land.': 1,
        'processtable.': 1,
        'smurf.': 1,
        'teardrop.': 1,
        'udpstorm.': 1,

        # R2L ATTACK
        'ftp_write.': 2,
        'guess_passwd.': 2,
        'imap.': 2,
        'multihop.': 2,  # disputation resolved
        'named.': 2,
        'phf.': 2,
        'sendmail.': 2,
        'snmpgetattack.': 2,
        'snmpguess.': 2,
        'worm.': 2,
        'xlock.': 2,
        'xsnoop.': 2,
        'spy.': 2,
        'warezclient.': 2,
        'warezmaster.': 2,  # disputation resolved

        # U2R ATTACK
        'httptunnel.': 3,  # disputation resolved
        'buffer_overflow.': 3,
        'loadmodule.': 3,
        'perl.': 3,
        'ps.': 3,
        'rootkit.': 3,
        'sqlattack.': 3,
        'xterm.': 3,

        # PROBING ATTACK
        'ipsweep.': 4,
        'mscan.': 4,
        'nmap.': 4,
        'portsweep.': 4,
        'saint.': 4,
        'satan.': 4,
    }
    l = []
    for val in df['attack_type']:
        l.append(d[val])
    tmp_df = pd.DataFrame(l, columns=['attack_type'])
    df = df.drop('attack_type', axis=1)
    df = df.join(tmp_df)
    return df


def one_hot(df):
    service_one_hot = pd.get_dummies(df["service"])
    df = df.drop('service', axis=1)
    df = df.join(service_one_hot)

    # test data has this column in service, clashes with protocol_type
    # and not seen in training data, won't be learn by the model, safely delete
    if 'icmp' in df.columns:
        df = df.drop('icmp', axis=1)

    protocol_type_one_hot = pd.get_dummies(df["protocol_type"])
    df = df.drop('protocol_type', axis=1)
    df = df.join(protocol_type_one_hot)

    flag_type_one_hot = pd.get_dummies(df["flag"])
    df = df.drop('flag', axis=1)
    df = df.join(flag_type_one_hot)
    return df
