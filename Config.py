import yaml
from yaml.parser import ParserError
from rich import print

from Exceptions.InvalidCredentialsException import InvalidCredentialsException
from Types.Config import Account, Config as ConfigType

class Config:
    """
    A class that loads and stores the configuration
    """

    def __init__(self, configPath: str) -> None:
        """
        Loads the configuration file into the Config object

        :param configPath: string, path to the configuration file
        """
        
        try:
            with open(configPath, "r",  encoding='utf-8') as f:
                config = yaml.safe_load(f)

                accs = config.get("accounts")

                accounts: dict[str, Account] = {}
                for account in accs:
                    accounts[account] = {
                        "username": accs[account]["username"],
                        "password": accs[account]["password"],
                    }
                    if "username" == accs[account]["username"]:
                        raise InvalidCredentialsException              

                debug = config.get("debug", False)
                connectorDrops = config.get("connectorDropsUrl", "")

                self.config = ConfigType(accounts, debug, connectorDrops)
        except FileNotFoundError as ex:
            print(f"[red]CRITICAL ERROR: The configuration file cannot be found at {configPath}\nHave you extacted the ZIP archive and edited the configuration file?")
            print("Press any key to exit...")
            input()
            raise ex
        except (ParserError, KeyError) as ex:
            print(f"[red]CRITICAL ERROR: The configuration file does not have a valid format.\nPlease, check it for extra spaces and other characters.\nAlternatively, use confighelper.html to generate a new one.")
            print("Press any key to exit...")
            input()
            raise ex
        except InvalidCredentialsException as ex:
            print(f"[red]CRITICAL ERROR: There are only default credentials in the configuration file.\nYou need to add you Riot account login to config.yaml to receive drops.")
            print("Press any key to exit...")
            input()
            raise ex
            
        with open("bestStreams.txt", "r",  encoding='utf-8') as f:
            self.bestStreams = f.read().splitlines()

    def getAccount(self, account: str) -> Account:
        """
        Get account information

        :param account: string, name of the account
        :return: dictionary, account information
        """
        return self.config.accounts[account]
