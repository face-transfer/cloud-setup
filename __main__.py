import pulumi
import pulumi_aws as aws


def create_bucket(project, name, versioning_enabled=True):
    original_images_bucket = aws.s3.Bucket(
        f"{project}-{name}",
        bucket=f"{project}-{name}",
        acl="private",
        versioning=aws.s3.BucketVersioningArgs(
            enabled=True,
        )
    )

    pulumi.export(f"{project}-{name}", original_images_bucket.id)


create_bucket("face-transfer", "origin-images")
create_bucket("face-transfer", "input-images")
create_bucket("face-transfer", "output-images")
