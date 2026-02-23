import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. ANDMETE LAADIMINE
def download_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    return df

# 2. FILTREERIMINE
def filter_country(df, country):
    return df[df["location"] == country]

# 3. ÜHE RIIGI ANALÜÜS
def analysis_country(df, country):
    data = df[df["location"] == country]
    max_infection = data["new_cases"].max()
    total_deaths = data["total_deaths"].max()
    total_infections = data["total_cases"].max()
    return f"{country} max infection was {max_infection}, total death was {total_deaths}, total infection was {total_infections}"

# 4. SURMADE ANALÜÜS
def death_rate(df, countrys):
    for r in countrys:
        data = df[df["location"] == r]
        total_deaths = data["total_deaths"].max()
        total_cases = data["total_cases"].max()
        death_rate = total_deaths / total_cases * 100
        print(f"{r}: death_rate {death_rate:.2f}%")

# 5. KORRELATSIOON
def correlation(df, countrys):
    for r in countrys:
        data = df[df["location"] == r]
        columns = ["new_cases_per_million", "new_deaths_per_million",
                  "total_vaccinations_per_hundred", "stringency_index"]
        abbreviations = {
            "new_cases_per_million": "nakatumised",
            "new_deaths_per_million": "surmad",
            "total_vaccinations_per_hundred": "vaktsineerimisi",
            "stringency_index": "piirangud"
        }
        correlation_matrix = data[columns].corr()
        correlation_matrix = correlation_matrix.rename(columns=abbreviations, index=abbreviations)
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title(f"Correlation matrix = {r}")
        plt.tight_layout()
        print("Close the graph window to continue...")
        plt.show()
        

# 6. countryIDE VÕRDLUS
def compare_countrys(df, countrys):
    for r in countrys:
        data = df[df["location"] == r]
        plt.plot(data["date"], data["new_cases_per_million"], label=r)
    plt.legend()
    print("Close the graph window to continue...")
    plt.show()

# 7. PÕHIPROGRAMM
if __name__ == "__main__":
    df = download_data()
    print("Welcome to Covid Analysis")
    while True:
        print("\nPress 1: One country analysis")
        print("Press 2: Death analysis for multiple countries")
        print("Press 3: Correlation on selected country")
        print("Press 4: Compare two countries")
        print("Press 5: Exit")
        user_input = int(input("Enter number 1 - 5: "))
        if user_input == 1:
            choose_country = input("Enter country name: ")
            print(analysis_country(df, choose_country))
        elif user_input == 2:
            choose_country_1 = input("Enter first country name: ")
            choose_country_2 = input("Enter second country name: ")
            choose_country_3 = input("Enter third country name: ")
            death_rate(df, [choose_country_1, choose_country_2, choose_country_3])
        elif user_input == 3:
            choose_country = input("Enter country name: ")
            correlation(df, [choose_country])
        elif user_input == 4:
            choose_country_1 = input("Enter first country name: ")
            choose_country_2 = input("Enter second country name: ")
            compare_countrys(df, [choose_country_1, choose_country_2])
        elif user_input == 5:
            print("Goodbye!")
            break