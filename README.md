## DNSControl Template
This template provides a starting point to use [DNSControl](https://github.com/stackexchange/dnscontrol) with gitlab CI/CD.

Provided are the following:

- `dnsconfig.js` - Nearly blank config file for DNS changes.
- `creds.json` - DNSControl authentication tokens/api credentials for your DNS and Registrar providers
- `presubmit.py` - Python script to check before submitting any changes into version control
- `.gitlab-ci.yml` - CI/CD configuration to actually test,preview and push changes.

### Getting Started

#### Prerequisites
DNSControl binary must be installed, this can be obtained from the releases page of the DNSControl repository or look at the [installation section.](https://github.com/StackExchange/dnscontrol#installation)


1. Clone this repository
2. Make sure DNSControl is installed
    ````
    dnscontrol version
    ````
3. Get an api token or api key from your DNS provider or registrar, the currently supported providers all have their own ways of doing this but you should look at restricting the key/token to only make DNS changes.
4. Fill out the `creds.json` file with your key/token, each provider requires a different name for their credentials so you should look at the [documentation provided.](https://stackexchange.github.io/dnscontrol/provider-list)

    For the pursposes of using version control plain-text secrets should be avoided at all costs, as such it is reccomended that environment variables are used as in the example cred.json file. These can be added to your CI/CD environment and to your shell when testing.

#### Existing DNS Records

5. Having existing records will mean the that the provided dnsconfig file would overwrite any DNS record you currently have, thus we must obtain the current record set from your provider.

6. Run `dnscontrol get-zones --format=djs --out dnsconfig-new.js`
    This will contact your provider, authenticate with the information in creds.json and retrieve your current record set in the dnsconfig.js format.

    Mistakes can happen, you should review the newly created `dnsconfig-new.js` file and only when happy overwrite the example dnsconfig.js file with this generated verion.

7. Now you can make changes, using the [language reference](https://stackexchange.github.io/dnscontrol/js) specify your DNS records, for example add a new TXT record with `dnscontrol-test`:
    ```
    ...
    TXT['@', 'dnscontrol-test'),
    ...
    ```
8. Check your changes beforehand with the `presubmit.py` script and `dnscontrol check` You should also preview the record changes with `dnscontrol preview` but note if 
you have included provider authentication as environment variables they will need to be added to shell that is using the dnscontrol command.

9. Once the changes look correct go ahead and push them to the provider who will make them live with `dnscontrol push` and all going well you should see the same output as the preview dry-run, only now they are changed on your provider. check with dig just to make sure.

#### New Domain

5. Without existing records this configuration should work out of the box once your creds.json file is populated, as such there is just a matter of adding and records to the dnsconfig.js file using the [language reference.](https://stackexchange.github.io/dnscontrol/js)

6. Check your changes beforehand with the `presubmit.py` script and `dnscontrol check` You should also preview the record changes with `dnscontrol preview` but note if 
you have included provider authentication as environment variables they will need to be added to shell that is using the dnscontrol command.

7. Once the changes look correct go ahead and push them to the provider who will make them live with `dnscontrol push` and all going well you should see the same output as the preview dry-run, only now they are changed on your provider. check with dig just to make sure.


