# A simple python webservice for DETA

Starting point for lots of cool stuff...

... running on [DETA](https://deta.sh)

## Requirements

 * **Flask** https://flask.palletsprojects.com/

## Local run configuration

Parameters: `-m flask run`

## Getting started

Install the deta client by executing `curl -fsSL https://get.deta.dev/cli.sh | sh`

```shell script
deta login
deta new --python <MICRO_NAME>
```

## Deploy

There are 2 ways to deploy. Both will deploy into a [Deta Micro](https://docs.deta.sh/docs/micros/about).

### Manual deploy

```shell script
deta deploy
```

### Automatic deploy

Via [github action](.github/workflows/deploy.yml).

Remember to create and set the `DETA_TOKEN` secret.

## Database

Database is a [_Deta Base_](https://docs.deta.sh/docs/base/about) :clown_face:

No configuration is needed other than Deta Base name.

