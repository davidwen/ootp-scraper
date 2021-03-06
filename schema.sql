CREATE TABLE IF NOT EXISTS players(
    id INTEGER PRIMARY KEY,
    name TEXT,
    birthday TEXT,
    leadership INTEGER,
    loyalty INTEGER,
    desire_for_win INTEGER,
    greed INTEGER,
    intelligence INTEGER,
    work_ethic INTEGER,
    bats TEXT,
    throws TEXT,
    position TEXT,
    retired INTEGER);

CREATE TABLE IF NOT EXISTS batting_stats(
    player_id INTEGER,
    position TEXT,
    start_year INTEGER,
    end_year INTEGER,
    g INTEGER,
    ab INTEGER,
    h INTEGER,
    double INTEGER,
    triple INTEGER,
    hr INTEGER,
    rbi INTEGER,
    r INTEGER,
    bb INTEGER,
    hp INTEGER,
    sf INTEGER,
    k INTEGER,
    sb INTEGER,
    cs INTEGER,
    vorp REAL,
    war REAL,
    avg REAL,
    obp REAL,
    slg REAL,
    ops REAL,
    babip REAL,
    krate REAL,
    bbrate REAL,
    PRIMARY KEY (player_id),
    FOREIGN KEY (player_id) REFERENCES players(id));

CREATE TABLE IF NOT EXISTS pitching_stats(
    player_id INTEGER,
    start_year INTEGER,
    end_year INTEGER,
    g INTEGER,
    gs INTEGER,
    w INTEGER,
    l INTEGER,
    sv INTEGER,
    outs INTEGER,
    ha INTEGER,
    r INTEGER,
    er INTEGER,
    hr INTEGER,
    bb INTEGER,
    k INTEGER,
    cg INTEGER,
    sho INTEGER,
    vorp REAL,
    war REAL,
    era REAL,
    whip REAL,
    k9 REAL,
    bb9 REAL,
    kbb REAL,
    PRIMARY KEY (player_id),
    FOREIGN KEY (player_id) REFERENCES players(id));

CREATE TABLE IF NOT EXISTS season_batting_stats(
    year INTEGER,
    player_id INTEGER,
    team_id INTEGER,
    position TEXT,
    g INTEGER,
    ab INTEGER,
    h INTEGER,
    double INTEGER,
    triple INTEGER,
    hr INTEGER,
    rbi INTEGER,
    r INTEGER,
    bb INTEGER,
    hp INTEGER,
    sf INTEGER,
    k INTEGER,
    sb INTEGER,
    cs INTEGER,
    vorp REAL,
    war REAL,
    avg REAL,
    obp REAL,
    slg REAL,
    ops REAL,
    babip REAL,
    krate REAL,
    bbrate REAL,
    PRIMARY KEY (player_id, year, team_id),
    FOREIGN KEY (player_id) REFERENCES players(id));

CREATE TABLE IF NOT EXISTS season_pitching_stats(
    year INTEGER,
    player_id INTEGER,
    team_id INTEGER,
    g INTEGER,
    gs INTEGER,
    w INTEGER,
    l INTEGER,
    sv INTEGER,
    outs INTEGER,
    ha INTEGER,
    r INTEGER,
    er INTEGER,
    hr INTEGER,
    bb INTEGER,
    k INTEGER,
    cg INTEGER,
    sho INTEGER,
    vorp REAL,
    war REAL,
    era REAL,
    whip REAL,
    k9 REAL,
    bb9 REAL,
    kbb REAL,
    PRIMARY KEY (player_id, year),
    FOREIGN KEY (player_id) REFERENCES players(id));

CREATE TABLE IF NOT EXISTS hall_of_fame (
    player_id INTEGER,
    year INTEGER,
    FOREIGN KEY (player_id) REFERENCES players(id));

CREATE TABLE IF NOT EXISTS hall_of_fame_eligible (
    player_id INTEGER,
    FOREIGN KEY (player_id) REFERENCES players(id));

CREATE TABLE IF NOT EXISTS dates(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT UNIQUE);

CREATE TABLE IF NOT EXISTS waiver_wire(
    date_id INTEGER,
    player_id INTEGER,
    PRIMARY KEY (player_id, date_id));

CREATE TABLE IF NOT EXISTS batting_ratings(
    player_id INTEGER,
    date_id INTEGER,
    contact INTEGER,
    gap INTEGER,
    power INTEGER,
    eye INTEGER,
    avoid_k INTEGER,
    contact_r INTEGER,
    gap_r INTEGER,
    power_r INTEGER,
    eye_r INTEGER,
    avoid_k_r INTEGER,
    contact_l INTEGER,
    gap_l INTEGER,
    power_l INTEGER,
    eye_l INTEGER,
    avoid_k_l INTEGER,
    pot_contact INTEGER,
    pot_gap INTEGER,
    pot_power INTEGER,
    pot_eye INTEGER,
    pot_avoid_k INTEGER,
    PRIMARY KEY (player_id, date_id),
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (date_id) REFERENCES dates(id));

CREATE TABLE IF NOT EXISTS pitching_ratings(
    player_id INTEGER,
    date_id INTEGER,
    stuff INTEGER,
    movement INTEGER,
    control INTEGER,
    stuff_l INTEGER,
    movement_l INTEGER,
    control_l INTEGER,
    stuff_r INTEGER,
    movement_r INTEGER,
    control_r INTEGER,
    pot_stuff INTEGER,
    pot_movement INTEGER,
    pot_control INTEGER,
    stamina INTEGER,
    velocity INTEGER,
    hold INTEGER,
    groundball INTEGER,
    PRIMARY KEY (player_id, date_id),
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (date_id) REFERENCES dates(id));

CREATE TABLE IF NOT EXISTS leagues(
    id INTEGER PRIMARY KEY,
    name TEXT,
    level TEXT,
    parent_id INTEGER,
    short_name TEXT,
    FOREIGN KEY (parent_id) REFERENCES leagues(id));

CREATE TABLE IF NOT EXISTS teams(
    id INTEGER PRIMARY KEY,
    name TEXT,
    level TEXT,
    parent_id INTEGER,
    league_id INTEGER,
    short_name TEXT,
    FOREIGN KEY (parent_id) REFERENCES teams(id));

CREATE TABLE IF NOT EXISTS team_leagues(
    team_id INTEGER,
    year INTEGER,
    league_id INTEGER,
    division TEXT,
    wins INTEGER,
    losses INTEGER,
    champion INTEGER,
    PRIMARY KEY (team_id, year),
    FOREIGN KEY (team_id) REFERENCES teams(id),
    FOREIGN KEY (league_id) REFERENCES leagues(id));

CREATE TABLE IF NOT EXISTS player_teams(
    player_id INTEGER,
    date_id INTEGER,
    team_id INTEGER,
    PRIMARY KEY (player_id, date_id),
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (date_id) REFERENCES dates(id),
    FOREIGN KEY (team_id) REFERENCES teams(id));

CREATE TABLE IF NOT EXISTS starred (
    player_id INTEGER,
    PRIMARY KEY (player_id));

CREATE TABLE IF NOT EXISTS payrolls (
    date_id INTEGER,
    team_id INTEGER,
    payroll INTEGER,
    PRIMARY KEY (date_id, team_id),
    FOREIGN KEY (date_id) REFERENCES dates(id),
    FOREIGN KEY (team_id) REFERENCES teams(id));

CREATE TABLE IF NOT EXISTS healed_players (
    date_id INTEGER,
    player_id INTEGER,
    PRIMARY KEY (date_id, player_id),
    FOREIGN KEY (date_id) REFERENCES dates(id),
    FOREIGN KEY (player_id) REFERENCES players(id));