from infrastructure.sqlite.database import database
from infrastructure.sqlite.repozitories.posts import PostRepozitory
from shemas.posts import Post as PostSchema
from core.exceptions.database_exceptions import PostAlreadyExistsException, PostNotFoundException
from core.exceptions.domain_exceptions import PostIdIsNotUniqueException, PostNotFoundByIdException

class ChangePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepozitory()

    async def execute(self, new_post: str) -> PostSchema:
        try:
            with self._database.session() as session:
                post = self._repo.change(session=session, post=new_post)
        except PostAlreadyExistsException:
            raise PostIdIsNotUniqueException
        return PostSchema.model_validate(obj=post)