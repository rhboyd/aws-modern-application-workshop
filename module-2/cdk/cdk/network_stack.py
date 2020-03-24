from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_iam as iam
)

class NetworkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.__vpc = ec2.Vpc(
            self,
            "VPC",
            nat_gateways=1,
            max_azs=2
        )

    @property
    def vpc(self) -> ec2.Vpc:
        return self.__vpc