<div id="top"></div>

<br />
<div align="center">
<img src="https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest/scale-to-width-down/85?cb=20210620062038"/>

An Unofficial REST API for <a href="https://playvalorant.com/">Valorant</a>


Built by <a href="https://github.com/axsddlr">Andre Saddler</a>
</br>
  <a href="https://heroku.com/deploy">
    <img src="https://www.herokucdn.com/deploy/button.png">
  </a>

</div>

### Features
This REST API provides you with some useful tools such as:
- Patch Notes
- Latest News

## Current Endpoints

### `/valorant/<locale>/patch-notes`

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- locale: 
<details>
  <summary>Click to expand!</summary>

      ar_AE
      de_DE 
      en_US 
      es_ES 
      es_MX 
      fr_FR 
      id_ID 
      it_IT 
      ja_JP 
      ko_KR 
      pl_PL 
      pt_BR 
      ru_RU 
      th_TH 
      tr_TR 
      vi_VN 
      zh_TW     
</details>



### Usage

```
python3 main.py
OR 
uvicorn main:app --reload --port 3000
```

## Contributing

Feel free to submit a [pull request](https://github.com/rehkloos/vlrggapi/pull/new/master) or an [issue](https://github.com/rehkloos/vlrggapi/issues/new)!

## License

The MIT License (MIT)