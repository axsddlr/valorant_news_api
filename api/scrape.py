import re

import httpx

from utils.utils import headers, get_soup, get_status


class Valo:
    @staticmethod
    def patch_notes(locale):
        URL = f"https://playvalorant.com/page-data/{locale}/news/game-updates/page-data.json"
        response = httpx.get(URL, headers=headers)
        responseJSON = response.json()
        status = response.status_code

        base_path = responseJSON["result"]["pageContext"]["data"]["articles"]

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

            if "Patch" in title:
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


if __name__ == '__main__':
    print(Valo.patch_notes("en-us"))
