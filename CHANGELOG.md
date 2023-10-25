# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Broken

- `tests` are not full updated and could be wrong

### Added

- bumper adds
  - create new file `settings.py`
    - holds config variables used over the complete project, which was before included in `__init.py__`
  - create new file `utils.py`
    - includes multi function used in the project, as the logger configuration
  - `web` api `plugins` extended with more api's
    - tested also with newer app version, see `README.md`
    - some new one (not all are functional and only base implemented)
      - **api**
        - `pim/voice/get`
        - `appsvr/improve`
        - `appsvr/ota/firmware`
        - `appsvr/device/blacklist/check`
        - `basis/dc/get-by-area`
        - `ecms/file/get/{id}`
        - `ecms/app/ad/res/v2`
        - `ecms/app/element/hint`
        - `ecms/app/resources`
        - `homed/home/create`
        - `homed/home/delete`
        - `homed/member/list`
        - `homed/device/move`
        - `neng/message/read`
        - `neng/v2/message/push`
        - `neng/v3/message/latest_by_did`
        - `neng/v3/message/list`
        - `neng/v3/product/msg/tabs`
        - `neng/v3/shareMsg/hasUnreadMsg`
        - `rapp/sds/user/data/del`
        - `sds/baidu/audio/getcred`
      - **v1**
        - `agreement/getUserAcceptInfo`
        - `common/getUserConfig`
        - `common/getBottomNavigateInfoList`
        - `common/getAboutBriefItem`
        - `intl/member/basicInfo`
        - `intl/member/signStatus`
        - `osmall/getCountryConfig`
        - `osmall/proxy/my/get-user-center-coupon-list`
        - `osmall/index/getLayout`
        - `osmall/proxy/cart/get-count`
        - `osmall/proxy/v2/web/benefit/get-benefits`
        - `osmall/proxy/order/list`
        - `userSetting/getMsgReceiveSetting`
        - `userSetting/saveUserSetting`
        - `/user/getMyUserMenuInfo`
        - `user/getMyUserMenuInfo`
      - **v2**
        - `member/getExpByScene`
        - `message/waterfallFlow`
        - `message/moduleConfiguration`
        - `user/checkAgreementBatch`
      - **v3**
        - `common/getBottomNavigateInfoList`
- conf adds
  - add this `CHANGELOG.md`
  - add `pyproject.toml`
  - add `create_cert.sh`
    - for create example cert for bumper
  - add `requirements-update.sh`
    - for fast create new `requirements.txt` and `requirements-dev.txt` with newest versions
  - add `.codecov.yml` and `.coveragerc`
  - add `.gitattributes`
  - .github adds
    - add `DISCUSSION_TEMPLATE`
    - add `ISSUE_TEMPLATE` as yaml and removed md one
    - add `PULL_REQUEST_TEMPLATE.md`
    - add workflow `release-drafter.yml`

### Changed

- bumper updates
  - created folder `utils` and moved the files `db.py` and `dns.py`
  - moved `models.py` into `web` folder
  - renamed `util.py` as `utils.py` and updated with additional more functions
  - moved `xmppserver.py` into folder `xmpp` as `xmpp.py`
  - multiple updates performed for all modules in `mqtt`, `web`, `xmpp` and `utils`
    - lint and prettier runnings
    - web `middleware` extended for more logging option, which can activated over env variables
    - additional strings moved into `settings` as variable
    - `xmpp` improved in `_handle_result` and `_handle_connect`
    - multiple small cleanups, adds and improves
  - `__init__.py` was shrunk and updated
  - `web` api `plugins` extended with more and updated api's
    - changed multi routes from `*` to `POST` as they defined to have a body
    - update some api with extended response
- conf updates
  - renamed `.prettierrc` to `.prettierrc.yml` and rewrite in yaml
  - renamed `bandit.yaml` to `bandit.yml`
  - renamed `LICENSE.txt` to `LICENSE`
  - update `setup.cfg`
    - flake8 changed line length to 130
    - isort add line-length as 130
  - update version in `requirements.txt`
  - update version in `requirements-dev.txt`
  - add additional information into `README.md`
  - update additional in `pylintrc`
    - updated good-names
    - updated disable
    - updated max-parents
    - added max-args
  - updated `mypy.ini` to python version 3.11
  - update `Dockerfile`
    - update from versions as variables
    - add labels
    - changed to work with bumper updates
  - moved `docker-compose.yaml` and extend with additional configs
  - moved `ngnix.conf` into new folder configs/ngnix
  - update `.gitignore`
  - update `.yamllint`
  - update `.pre-commit-config.yaml`
    - version updates
    - additional args added
  - updated `CmdLine.md` by add sh to code block
  - update `Env_Var.md`
  - .github updates
    - update workflow `ci.yml`
      - with new version, comments
      - update build step for docker build and push to ghcr.io
    - update workflow `codeql-analysis.yml`

### Removed

- conf files removed
  - `.dockerfile`
  - `requirements-test.txt`
  - removed `README.md` from data folder and add `.gitempty`
  - removed `README.md` from logs folder and add `.gitempty`
  - removed `README.md` from certs folder and add `.gitempty`
  - .github removes
    - remove `md` files from `ISSUE_TEMPLATE`, replaced with new `yaml` templates

[unreleased]: https://github.com/edenhaus/bumper/compare/dev...MVladislav:bumper:dev