import os
import sys
from os import path
import json
from traitlets import Bool, Int, Unicode, List, Dict, Float
from traitlets.config import Application, Configurable, catch_config_error


class NoStart(Exception):
    """Exception to raise when an application shouldn't start"""


class RecipeArgs(Configurable):
    lot_id = Unicode("UNKNOWN_LOTID", help="LOT ID").tag(config=True)
    step_id = Unicode("UNKNOWN_STEPID", help="STEP ID").tag(config=True)
    grpc_ip = Unicode("127.0.0.1:8080", help="GRPC Host 'IP:Port'").tag(config=True)
    job_id = Unicode("no-job-id", help="Job Id").tag(config=True)
    sub_job_id = Unicode("no-sub-job-id", help="Sub Job Id").tag(config=True)


class SraParameter(Configurable):
    use_shot_map = Bool(True, help="Use Shot Map").tag(config=True)
    cluster_method = Unicode('accurate', help="Clustering Algorithm(accurate, normal, special)").tag(config=True)


class DsaParameter(Configurable):
    step_ordering = Bool(default_value=True, help="Step Ordering Option").tag(config=True)
    cluster_method = Unicode('accurate', help="Clustering Algorithm(accurate, normal, special)").tag(config=True)
    cluster_distance = Float(1000.0, help="Cluster Radius Distance").tag(config=True)


def _generation_confirmed(config_file_name):
    generate = False
    if os.path.exists(config_file_name):
        reply = None
        while reply is None:
            reply = input(f'overwrite configuration file at ({config_file_name}) ([y]/n) ?').lower().strip()
            if reply == "n":
                return
            elif reply == "y" or reply == "":
                generate = True
                break
            else:
                reply = None
    else:
        generate = True
    return generate


class CommonSubApp(Application):
    flags = {
        'generate-config': ({'CommonSubApp': {'generate_config': True}}, "generate default config file"),
    }
    generate_config = Bool(False, help="Generate Config File").tag(config=True)
    classes = List([RecipeArgs])

    @catch_config_error
    def initialize(self, argv=None):
        super(CommonSubApp, self).initialize(argv)
        if self.generate_config:
            self.configure()  # 기본값이 설정된다.
            self.create_config_file()
            self.exit(1)
        elif self.config_file:
            # 설정 파일 검색시 사용할 경로들
            config_search_paths = [
                os.getcwd()
            ]
            self.load_config_file(self.config_file, config_search_paths)
            self.configure()
            pass

    def start(self):
        # 각 CommonSubApp 파생 클래스는 process()를 반드시 가져야 한다.
        self.process()

    def configure(self):
        self.recipe_args = RecipeArgs(config=self.config)

    def process(self):
        # 여기로 들어오면 자식 클래스가 process()를 구현 안했다는...
        pass

    def to_json_config(self):
        config = {}
        for key in self.__dict__.keys():
            configurable = getattr(self, key)
            if not isinstance(configurable, Configurable):
                continue
            config_data = {}
            for config_key in filter(lambda x: x not in ['parent', 'config'], configurable.trait_names()):
                config_data[config_key] = getattr(configurable, config_key)
            config[configurable.__class__.__name__] = config_data
        return json.dumps(config, indent=2)

    def create_config_file(self):
        config_file_name = f'{os.getcwd()}\\{self.config_file}.json'
        if _generation_confirmed(config_file_name):
            print('generating configuration : ', config_file_name)
            with open(config_file_name, 'w') as f:
                f.write(self.to_json_config())


class SraApp(CommonSubApp):
    name = "sra"
    classes = List([SraParameter])
    config_file = Unicode('dsa_config', help="SRA Configuration FileName").tag(config=True)

    def configure(self):
        super(SraApp, self).configure()
        self.parameter = DsaParameter(config=self.config)

    def process(self):
        # super(DsaApp, self).start() --> 'dsa' subcommand 가 있는 경우..? 사용
        print('starting SRA... ')
        print(self.to_json_config())
        print('finished SRA.')


class DsaApp(CommonSubApp):
    name = "dsa"
    classes = List([DsaParameter])
    config_file = Unicode('dsa_config', help="DSA Configuration FileName").tag(config=True)

    def configure(self):
        super(DsaApp, self).configure()
        self.parameter = DsaParameter(config=self.config)

    def process(self):
        # super(DsaApp, self).start() --> 'dsa' subcommand 가 있는 경우..? 사용
        print('starting dsa... ')
        print(self.to_json_config())
        print('finished dsa.')


class MidewsApp(Application):
    name = "midews"
    # noinspection PyTypeChecker
    subcommands = Dict({
        'dsa': (DsaApp, "Midews DSA app"),
        'sra': (SraApp, "Midews SRA app")
    })

    def start(self):
        if self.subapp is None:
            print("No subcommand specified. Must specify one of: %s" % (self.subcommands.keys()))
            print()
            self.print_description()
            self.print_subcommands()
            self.exit(1)
        else:
            return self.subapp.start()


def main():
    MidewsApp.launch_instance()


if __name__ == "__main__":
    main()