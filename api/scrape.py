import httpx

from utils.utils import headers, get_status


def get_esports_news_json():
    url = "https://cdn.contentstack.io/v3/content_types/articles/entries?environment=production&locale=en-us"
    headers2 = {'access_token': "cs61908494445448f776bbdbc7", 'api_key': "bltb730eada072bdbf4"}

    response = httpx.get(url, headers=headers2)
    return response.json()


# def get_esports_schedule_json(region):
#     url = "https://esports-api.service.valorantesports.com/persisted/val/getSchedule"
#     region = res.region[str(region)]
#
#     # gc_na = 106976737954740691
#     # na = 105555635175479654
#     querystring = {"hl": "en-US", "sport": "val", "leagueId": f"{region}"}
#
#     headers2 = {
#         'authority': "esports-api.service.valorantesports.com",
#         'accept': "*/*",
#         'accept-language': "en-US,en;q=0.9",
#         'cache-control': "no-cache",
#         'origin': "https://valorantesports.com",
#         'pragma': "no-cache",
#         'referer': "https://valorantesports.com/",
#         'sec-ch-ua': "^\^",
#         'x-api-key': f"{ESKEY}"
#     }
#     response = httpx.get(url, headers=headers2, params=querystring)
#     return response


class Valo:
    @staticmethod
    def get_esports_news():
        apiResponse = get_esports_news_json()
        base = apiResponse["entries"]

        status = get_status("https://playvalorant.com/en-us/news/")

        api = []
        for each in base:
            description = each["description"]
            title = each["title"]
            date = each["date"]
            url = each["url"]["url"]
            thumbnail = each["banner_settings"]["banner"]["url"]

            api.append(
                {
                    "title": title,
                    "summary": description,
                    "created_at": date,
                    "url": url,
                    "thumbnail": thumbnail,
                }
            )

        data = {"status": status, "data": api}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

    @staticmethod
    def get_news(locale):
        URL = f"https://playvalorant.com/page-data/{locale}/news/page-data.json"
        response = httpx.get(URL, headers=headers)
        responseJSON = response.json()
        status = response.status_code

        base_path = responseJSON["result"]["data"]["allContentstackArticles"]["nodes"]

        api = []
        for each in base_path:
            # print(each["title"])
            title = each["title"]
            title = title.replace("\u2019", "'")
            description = each["description"]
            description = description.replace("\u2019", "'")
            thumbnail = each["banner"]["url"]
            url_path = each["url"]["url"]
            external_link = each["external_link"]
            category = each["category"][0]["title"]

            if "Patch" not in title:
                api.append(
                    {
                        "title": title,
                        "description": description,
                        "thumbnail": thumbnail,
                        "url_path": url_path,
                        "external_link": external_link,
                        "category": category,
                    }
                )

        data = {"status": status, "data": api}

        return data

    @staticmethod
    def get_patch_notes(locale):
        URL = f"https://playvalorant.com/page-data/{locale}/news/tags/patch-notes/page-data.json"
        response = httpx.get(URL, headers=headers)
        responseJSON = response.json()
        status = response.status_code

        base_path = responseJSON["result"]["data"]["articles"]["nodes"]

        api = []
        for each in base_path:
            # print(each["title"])
            title = each["title"]
            title = title.replace("\u2019", "'")
            description = each["description"]
            description = description.replace("\u2019", "'")
            thumbnail = each["banner"]["url"]
            url_path = each["url"]["url"]
            external_link = each["external_link"]
            category = each["category"][0]["title"]

            api.append(
                {
                    "title": title,
                    "description": description,
                    "thumbnail": thumbnail,
                    "url_path": url_path,
                    "external_link": external_link,
                    "category": category,
                }
            )

        data = {"status": status, "data": api}

        return data

    # @staticmethod
    # def get_esports_schedule(region, stateof):
    #     apiResponse = get_esports_schedule_json(region).json()
    #     status = get_esports_schedule_json(region).status_code
    #     try:
    #         base = apiResponse["data"]["schedule"]["events"]
    #     except KeyError:
    #         base = None
    #
    #     tournament_info = []
    #
    #     for each in base:
    #         start_time = each["startTime"]
    #         state = each["state"]
    #         region = each["league"]["region"]
    #         stage = each["tournament"]["split"]["name"]
    #         teams = each["match"]["teams"]
    #
    #         if f"{stateof}" in state:
    #             tournament_info.append(
    #                 {
    #                     "title": start_time,
    #                     "region": region,
    #                     "stage": stage,
    #                     "teams": teams,
    #                 }
    #             )
    #         data = {"status": status, "data": tournament_info}
    #     return data


if __name__ == '__main__':
    print(Valo.get_esports_news())
