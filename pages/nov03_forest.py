"""Forest app alternatives on iPhone, EN. Our app: 3 Tasks (id1553693943), a three-task list with a timer on each; it
does not block apps or grow trees, and the page says so.

Checked 2026-11-03: US App Store search for «forest focus», «focus timer», «pomodoro», «stay focused», «study timer»,
iTunes lookup and the US App Store page of every app (price list, privacy label). reviewland's to-do pages (simple
to-do lists, Todoist alternatives) list task managers, none of these focus timers apart from 3 Tasks. Why this topic:
Google suggests «forest app alternative», «forest app alternatives», «forest app alternative ios», «... free» (3 Nov);
no page on the 4 sites is about Forest. Registered in ios-playbook references/temas-webs.md (f135c7d). Nothing tested.
"""

D = "2026-11-03"
CHECKED = "2026-11-03"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f}"]}
    if ours:
        a["ours"] = True
    return a


NL = "Data Not Linked to You"
TN = "Data Used to Track You; Data Not Linked to You"
T3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"

PAGES = [{
    "group": "forest-alt", "lang": "en", "store": "us",
    "path": "forest-app-alternatives-iphone/",
    "ct": "rd-forest-alt-iphone",
    "category": "ProductivityApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Forest App Alternatives for iPhone (2026): 7 Focus Timers",
    "h1": "Best Forest app alternatives for iPhone in 2026",
    "description": "Forest grows a tree while you stay off your phone. Seven iPhone focus timers compared: app blocking, to-do lists, lifetime prices and privacy labels.",
    "llms": "Compares seven iPhone alternatives to Forest (focus timer that grows a tree while you stay off your phone; free with a subscription and in-app items, privacy label with tracking): Flora (free, trees with friends, to-do list), Focus Friend (a Bean you decorate, by Hank Green), Focus To-Do (Pomodoro plus task manager), 3 Tasks (three tasks a day with a timer on each), FocusFlight (sessions as flights), Focus Keeper (classic Pomodoro) and Focus Plant (plants and worlds), by app blocking, to-do list, price and App Store privacy label.",
    "llms_note": "3 Tasks, one of the seven, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>Forest grows a virtual tree while you stay off your phone and kills it if you leave early</strong>; it can block apps from an Allow List and plants real trees with Trees for the Future. On the US App Store (3 November 2026) it is free to download, with a subscription listed at $5.99 a month or $35.99 a year («Early Bird» prices) and in-game items, and its privacy label includes <em>Data Used to Track You</em>.",
        "For the same idea for free, Flora grows trees with friends and adds a to-do list. Focus Friend swaps the tree for a Bean you decorate, and Focus Plant for plants and worlds. If what you need is to finish tasks rather than avoid your phone, Focus To-Do pairs a Pomodoro timer with a task manager, and 3 Tasks keeps you to three tasks a day with a timer on each. FocusFlight and Focus Keeper are timers first. Focus Friend, Focus To-Do and FocusFlight list only Data Not Linked to You.",
    ],
    "columns": ["App", "Price (US)", "Blocks apps, per its listing", "To-do list", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Forest for comparison: $5.99 a month or $35.99 a year, plus items. Ratings are that day's App Store average and count.",
    "apps": [
        app("Flora - Green Focus", 1225155794, "flora", "AppFinca Inc.", 4.76, 82948,
            "Forest's idea for free, with friends and a to-do list.",
            ["Plant a seed and it grows while you stay off the phone; leave and the tree dies.",
             "Plant together with friends, chat and share progress.",
             "A to-do list with reminders and a widget; tag trees with a task. Only small optional purchases listed."],
            "it is a large download (693 MB), it is in 3 languages, and its privacy label includes Data Used to Track You.",
            ["Optional tours $0.99 to $1.99",
             "Yes", "Yes", T3, "3.7.43 (30 Oct 2026)"]),
        app("Focus Friend, by Hank Green", 6742278016, "focus-friend", "B-Tech Consulting Group LLC", 4.83, 9819,
            "a cute Bean instead of a tree, with a lifetime price.",
            ["Stop the timer early and your Bean is sad; finish and you earn decorations for its room.",
             "Deep Focus Mode locks distracting apps; Pomodoro breaks; Live Activity on the lock screen.",
             "Pro is $3.99 a month, $19.99 a year or $39.99 lifetime."],
            "English only, a large download (399 MB), and no to-do list in its listing.",
            ["Pro $3.99 a month, $19.99 a year, lifetime $39.99; bean packs from $2.99",
             "Yes (Deep Focus Mode)", "No", NL, "1.28.2 (27 Oct 2026)"]),
        app("Focus To-Do: Focus Timer&Tasks", 966057213, "focus-to-do", "Shenzhen Tomato Software Technology Co., Ltd.", 4.8, 14712,
            "a Pomodoro timer and a full task manager in one, synced with your computer.",
            ["Pomodoro timer with custom lengths, short and long breaks and a continuous mode.",
             "Tasks, projects, reminders, recurring tasks and time tracking; syncs with a computer.",
             "Lifetime premium is listed at $11.99, in 33 languages."],
            "no app blocking or game in its listing; it is a planner more than a phone-free timer.",
            ["Lifetime $11.99; 3 months $3.99",
             "No", "Yes, full task manager", NL, "8.8 (21 Sep 2026)"]),
        app("To Do List & Focus: 3 Tasks", 1553693943, "3-tasks", "Saga Ltd.", 5.0, 5,
            "three tasks a day with a timer on each, free, and a one-time Pro.",
            ["Write three tasks each day and finish them one at a time, with a start and pause timer on each that keeps counting with the screen locked.",
             "Tasks that repeat daily, a home screen widget and dark mode, all free.",
             "Pro is a one-time purchase ($4.99 or $9.99 listed): history, streaks, CSV export and color themes."],
            "it does not block apps or grow anything, and its privacy label includes Data Used to Track You (Firebase Analytics, per its listing).",
            ["Pro one-time $4.99 or $9.99",
             "No", "Yes, three tasks a day", TN, "1.4.3 (26 Oct 2026)"], ours=True),
        app("FocusFlight - Deepfocus Timer", 6648771147, "focusflight", "Cement Planet LTD", 4.85, 9822,
            "turning each session into a flight on a 3D map, with app blocking.",
            ["Board, take off and land: each focus session is a flight you watch on a 3D map.",
             "«Airplane Mode» blocks distracting apps and websites through Apple's Screen Time.",
             "Lifetime listed from $18.99 to $33.99."],
            "a large download (273 MB), in 6 languages, and no to-do list beyond choosing a task.",
            ["Monthly $3.99, yearly $18.99, lifetime $18.99 to $33.99",
             "Yes", "Task per session", NL, "2.1.1 (1 Nov 2026)"]),
        app("Focus Keeper - Pomodoro Timer", 867374917, "focus-keeper", "PIXO Incorporation", 4.79, 31740,
            "the classic 25-minute Pomodoro, with charts of your focus time.",
            ["25-minute sessions with short and long breaks, all adjustable.",
             "Charts of your focus time over days and weeks.",
             "In 12 languages."],
            "a large download (914 MB), Pro prices up to $199.99, no app blocking in its listing, and its privacy label includes Data Used to Track You.",
            ["Pro $3.99 to $12.99 a month, $34.99 to $69.99 a year; $99.99 or $199.99",
             "No", "No", TN, "4.2.21 (27 Oct 2026)"]),
        app("Focus Plant：forest app blocker", 1459096306, "focus-plant", "Shikudo Co., Ltd.", 4.72, 5463,
            "collecting plants and restoring worlds, if Forest's game is what keeps you going.",
            ["Focus time turns into raindrops that grow plants; hundreds to collect and worlds to clean up.",
             "Records of your focus time; reads mindful minutes from Forest and other apps through HealthKit.",
             "In 14 languages; runs on iOS 13."],
            "ads unless you subscribe ($4.99 a month to remove them), many packs and passes for sale, and its privacy label includes Data Used to Track You.",
            ["Remove ads $4.99 a month; passport $4.99 to $39.99; packs from $0.99",
             "Not named", "No", T3, "4.6 (2 Nov 2026)"]),
    ],
    "who": [
        "<strong>Forest's idea, free, with friends:</strong> Flora.",
        "<strong>A Bean instead of a tree:</strong> Focus Friend.",
        "<strong>Timer plus a full task manager:</strong> Focus To-Do.",
        "<strong>Just three tasks a day, timed:</strong> 3 Tasks.",
        "<strong>Sessions as flights, with blocking:</strong> FocusFlight.",
        "<strong>Classic Pomodoro:</strong> Focus Keeper.",
    ],
    "cases": ["Studying for exams without checking your phone.", "Finishing the three things that matter today.", "Leaving Forest's subscription for a one-time price."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «forest focus», «focus timer», «pomodoro», «stay focused» and «study timer», and read Forest's and each app's US App Store page and Apple's lookup data. «Blocks apps» means its listing says so. We tested nothing.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there a free alternative to Forest?",
         "Flora is free, with only small optional purchases listed. 3 Tasks keeps its three tasks, timers and widget free. The others are free to download with paid upgrades."),
        ("Which Forest alternatives block apps?",
         "Flora, Focus Friend (Deep Focus Mode) and FocusFlight («Airplane Mode») say they block distracting apps. Focus To-Do, 3 Tasks and Focus Keeper are timers without blocking."),
        ("Which have a one-time price instead of a subscription?",
         "3 Tasks Pro ($4.99 or $9.99), Focus To-Do ($11.99), FocusFlight (from $18.99) and Focus Friend ($39.99) list a lifetime or one-time purchase."),
        ("Which ones combine a focus timer with a to-do list?",
         "Focus To-Do has a full task manager, Flora a to-do list with reminders, and 3 Tasks a list of three tasks a day with a timer on each."),
    ],
    "sources": [
        ("Forest (App Store)", "https://apps.apple.com/us/app/id866450515"),
        ("Flora (App Store)", "https://apps.apple.com/us/app/id1225155794"),
        ("Focus Friend (App Store)", "https://apps.apple.com/us/app/id6742278016"),
        ("Focus To-Do (App Store)", "https://apps.apple.com/us/app/id966057213"),
        ("3 Tasks (App Store)", "https://apps.apple.com/us/app/id1553693943"),
        ("FocusFlight (App Store)", "https://apps.apple.com/us/app/id6648771147"),
        ("Focus Keeper (App Store)", "https://apps.apple.com/us/app/id867374917"),
        ("Focus Plant (App Store)", "https://apps.apple.com/us/app/id1459096306"),
    ],
}]
