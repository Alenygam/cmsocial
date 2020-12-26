"""The first migration. It's supposed to be run on an empty database.

Revision ID: 08a10b5b0f10
Revises:
Create Date: 2015-12-24 01:33:39.988635

"""

# revision identifiers, used by Alembic.
revision = '08a10b5b0f10'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
from sqlalchemy.dialects.postgresql import ENUM
import sqlalchemy as sa
import cms


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('hidden', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('_id', 'id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Unicode(), nullable=False),
    sa.Column('last_name', sa.Unicode(), nullable=False),
    sa.Column('username', sa.Unicode(), nullable=False),
    sa.Column('password', sa.Unicode(), nullable=False),
    sa.Column('email', sa.Unicode(), nullable=True),
    sa.Column('timezone', sa.Unicode(), nullable=True),
    sa.Column('preferred_languages', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('regions',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('_id', 'id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('fsobjects',
    sa.Column('digest', sa.String(), nullable=False),
    sa.Column('loid', sa.Integer(), nullable=False),
    sa.Column('description', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('digest')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Unicode(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('contests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=False),
    sa.Column('description', sa.Unicode(), nullable=False),
    sa.Column('allowed_localizations', cms.db.types.RepeatedUnicode(), nullable=False),
    sa.Column('languages', cms.db.types.RepeatedUnicode(), nullable=False),
    sa.Column('submissions_download_allowed', sa.Boolean(), nullable=False),
    sa.Column('ip_autologin', sa.Boolean(), nullable=False),
    sa.Column('token_mode', sa.Enum('disabled', 'finite', 'infinite', name='token_mode'), nullable=False),
    sa.Column('token_max_number', sa.Integer(), nullable=True),
    sa.Column('token_min_interval', sa.Interval(), nullable=False),
    sa.Column('token_gen_initial', sa.Integer(), nullable=False),
    sa.Column('token_gen_number', sa.Integer(), nullable=False),
    sa.Column('token_gen_interval', sa.Interval(), nullable=False),
    sa.Column('token_gen_max', sa.Integer(), nullable=True),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('stop', sa.DateTime(), nullable=False),
    sa.Column('timezone', sa.Unicode(), nullable=True),
    sa.Column('per_user_time', sa.Interval(), nullable=True),
    sa.Column('max_submission_number', sa.Integer(), nullable=True),
    sa.Column('max_user_test_number', sa.Integer(), nullable=True),
    sa.Column('min_submission_interval', sa.Interval(), nullable=True),
    sa.Column('min_user_test_interval', sa.Interval(), nullable=True),
    sa.Column('score_precision', sa.Integer(), nullable=False),
    sa.CheckConstraint('start <= stop'),
    sa.CheckConstraint('token_gen_initial <= token_gen_max'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('announcements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('subject', sa.Unicode(), nullable=False),
    sa.Column('text', sa.Unicode(), nullable=False),
    sa.Column('contest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contest_id'], ['contests.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_announcements_contest_id', 'announcements', ['contest_id'], unique=False)
    op.create_table('participations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.Unicode(), nullable=True),
    sa.Column('starting_time', sa.DateTime(), nullable=True),
    sa.Column('delay_time', sa.Interval(), nullable=False),
    sa.Column('extra_time', sa.Interval(), nullable=False),
    sa.Column('password', sa.Unicode(), nullable=True),
    sa.Column('hidden', sa.Boolean(), nullable=False),
    sa.Column('contest_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contest_id'], ['contests.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contest_id', 'user_id')
    )
    op.create_index('ix_participations_contest_id', 'participations', ['contest_id'], unique=False)
    op.create_index('ix_participations_user_id', 'participations', ['user_id'], unique=False)
    op.create_table('provinces',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['region_id'], ['regions.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('_id', 'id'),
    sa.UniqueConstraint('id')
    )
    op.create_index('ix_provinces_region_id', 'provinces', ['region_id'], unique=False)
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('contest_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.Unicode(), nullable=False),
    sa.Column('title', sa.Unicode(), nullable=False),
    sa.Column('primary_statements', sa.String(), nullable=False),
    sa.Column('token_mode', sa.Enum('disabled', 'finite', 'infinite', name='token_mode'), nullable=False),
    sa.Column('token_max_number', sa.Integer(), nullable=True),
    sa.Column('token_min_interval', sa.Interval(), nullable=False),
    sa.Column('token_gen_initial', sa.Integer(), nullable=False),
    sa.Column('token_gen_number', sa.Integer(), nullable=False),
    sa.Column('token_gen_interval', sa.Interval(), nullable=False),
    sa.Column('token_gen_max', sa.Integer(), nullable=True),
    sa.Column('max_submission_number', sa.Integer(), nullable=True),
    sa.Column('max_user_test_number', sa.Integer(), nullable=True),
    sa.Column('min_submission_interval', sa.Interval(), nullable=True),
    sa.Column('min_user_test_interval', sa.Interval(), nullable=True),
    sa.Column('score_precision', sa.Integer(), nullable=False),
    sa.Column('score_mode', sa.Enum('max_tokened_last', 'max', name='score_mode'), nullable=False),
    sa.Column('active_dataset_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('token_gen_initial <= token_gen_max'),
    sa.ForeignKeyConstraint(['contest_id'], ['contests.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id', 'active_dataset_id'], ['datasets.task_id', 'datasets.id'], name='fk_active_dataset_id', onupdate='SET NULL', ondelete='SET NULL', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contest_id', 'name'),
    sa.UniqueConstraint('contest_id', 'num'),
    sa.UniqueConstraint('name')
    )
    op.create_index('ix_tasks_contest_id', 'tasks', ['contest_id'], unique=False)
    op.create_table('attachments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.Unicode(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('task_id', 'filename')
    )
    op.create_index('ix_attachments_task_id', 'attachments', ['task_id'], unique=False)
    op.create_table('social_tasks',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_level', sa.Integer(), nullable=False),
    sa.Column('help_available', sa.Boolean(), nullable=False),
    sa.Column('nsubs', sa.Integer(), nullable=False),
    sa.Column('nsubscorrect', sa.Integer(), nullable=False),
    sa.Column('nusers', sa.Integer(), nullable=False),
    sa.Column('nuserscorrect', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('_id', 'id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('datasets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Unicode(), nullable=False),
    sa.Column('autojudge', sa.Boolean(), nullable=False),
    sa.Column('time_limit', sa.Float(), nullable=True),
    sa.Column('memory_limit', sa.Integer(), nullable=True),
    sa.Column('task_type', sa.String(), nullable=False),
    sa.Column('task_type_parameters', sa.String(), nullable=False),
    sa.Column('score_type', sa.String(), nullable=False),
    sa.Column('score_type_parameters', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id', 'task_id'),
    sa.UniqueConstraint('task_id', 'description')
    )
    op.create_table('cities',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('province_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['province_id'], ['provinces.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('_id', 'id'),
    sa.UniqueConstraint('id')
    )
    op.create_index('ix_cities_province_id', 'cities', ['province_id'], unique=False)
    op.create_table('submission_format_elements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.Unicode(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_submission_format_elements_task_id', 'submission_format_elements', ['task_id'], unique=False)
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('subject', sa.Unicode(), nullable=False),
    sa.Column('text', sa.Unicode(), nullable=False),
    sa.Column('participation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['participation_id'], ['participations.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_messages_participation_id', 'messages', ['participation_id'], unique=False)
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_timestamp', sa.DateTime(), nullable=False),
    sa.Column('subject', sa.Unicode(), nullable=False),
    sa.Column('text', sa.Unicode(), nullable=False),
    sa.Column('reply_timestamp', sa.DateTime(), nullable=True),
    sa.Column('ignored', sa.Boolean(), nullable=False),
    sa.Column('reply_subject', sa.Unicode(), nullable=True),
    sa.Column('reply_text', sa.Unicode(), nullable=True),
    sa.Column('participation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['participation_id'], ['participations.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_questions_participation_id', 'questions', ['participation_id'], unique=False)
    op.create_table('statements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('language', sa.Unicode(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('task_id', 'language')
    )
    op.create_index('ix_statements_task_id', 'statements', ['task_id'], unique=False)
    op.create_table('submissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participation_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('language', sa.String(), nullable=True),
    sa.Column('comment', sa.Unicode(), nullable=False),
    sa.ForeignKeyConstraint(['participation_id'], ['participations.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_submissions_participation_id', 'submissions', ['participation_id'], unique=False)
    op.create_index('ix_submissions_task_id', 'submissions', ['task_id'], unique=False)
    op.create_table('user_tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participation_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('language', sa.String(), nullable=True),
    sa.Column('input', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['participation_id'], ['participations.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_tests_participation_id', 'user_tests', ['participation_id'], unique=False)
    op.create_index('ix_user_tests_task_id', 'user_tests', ['task_id'], unique=False)
    op.create_table('printjobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participation_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('filename', sa.Unicode(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.Column('status', sa.Unicode(), nullable=True),
    sa.ForeignKeyConstraint(['participation_id'], ['participations.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_printjobs_participation_id', 'printjobs', ['participation_id'], unique=False)
    op.create_table('submission_results',
    sa.Column('submission_id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('compilation_outcome', sa.String(), nullable=True),
    sa.Column('compilation_text', sa.String(), nullable=True),
    sa.Column('compilation_tries', sa.Integer(), nullable=False),
    sa.Column('compilation_stdout', sa.Unicode(), nullable=True),
    sa.Column('compilation_stderr', sa.Unicode(), nullable=True),
    sa.Column('compilation_time', sa.Float(), nullable=True),
    sa.Column('compilation_wall_clock_time', sa.Float(), nullable=True),
    sa.Column('compilation_memory', sa.Integer(), nullable=True),
    sa.Column('compilation_shard', sa.Integer(), nullable=True),
    sa.Column('compilation_sandbox', sa.Unicode(), nullable=True),
    sa.Column('evaluation_outcome', sa.String(), nullable=True),
    sa.Column('evaluation_tries', sa.Integer(), nullable=False),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('score_details', sa.String(), nullable=True),
    sa.Column('public_score', sa.Float(), nullable=True),
    sa.Column('public_score_details', sa.String(), nullable=True),
    sa.Column('ranking_score_details', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['submission_id'], ['submissions.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('submission_id', 'dataset_id'),
    sa.UniqueConstraint('submission_id', 'dataset_id')
    )
    op.create_table('testcases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('codename', sa.Unicode(), nullable=False),
    sa.Column('public', sa.Boolean(), nullable=False),
    sa.Column('input', sa.String(), nullable=False),
    sa.Column('output', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dataset_id', 'codename')
    )
    op.create_index('ix_testcases_dataset_id', 'testcases', ['dataset_id'], unique=False)
    op.create_table('user_test_results',
    sa.Column('user_test_id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('output', sa.String(), nullable=True),
    sa.Column('compilation_outcome', sa.String(), nullable=True),
    sa.Column('compilation_text', sa.String(), nullable=True),
    sa.Column('compilation_tries', sa.Integer(), nullable=False),
    sa.Column('compilation_stdout', sa.Unicode(), nullable=True),
    sa.Column('compilation_stderr', sa.Unicode(), nullable=True),
    sa.Column('compilation_time', sa.Float(), nullable=True),
    sa.Column('compilation_wall_clock_time', sa.Float(), nullable=True),
    sa.Column('compilation_memory', sa.Integer(), nullable=True),
    sa.Column('compilation_shard', sa.Integer(), nullable=True),
    sa.Column('compilation_sandbox', sa.String(), nullable=True),
    sa.Column('evaluation_outcome', sa.String(), nullable=True),
    sa.Column('evaluation_text', sa.String(), nullable=True),
    sa.Column('evaluation_tries', sa.Integer(), nullable=False),
    sa.Column('execution_time', sa.Float(), nullable=True),
    sa.Column('execution_wall_clock_time', sa.Float(), nullable=True),
    sa.Column('execution_memory', sa.Integer(), nullable=True),
    sa.Column('evaluation_shard', sa.Integer(), nullable=True),
    sa.Column('evaluation_sandbox', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_test_id'], ['user_tests.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_test_id', 'dataset_id'),
    sa.UniqueConstraint('user_test_id', 'dataset_id')
    )
    op.create_table('user_test_files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_test_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_test_id'], ['user_tests.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_test_id', 'filename')
    )
    op.create_index('ix_user_test_files_user_test_id', 'user_test_files', ['user_test_id'], unique=False)
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submission_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.Unicode(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['submission_id'], ['submissions.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('submission_id', 'filename')
    )
    op.create_index('ix_files_submission_id', 'files', ['submission_id'], unique=False)
    op.create_table('institutes',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('_id', 'id'),
    sa.UniqueConstraint('id')
    )
    op.create_index('ix_institutes_city_id', 'institutes', ['city_id'], unique=False)
    op.create_table('user_test_managers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_test_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_test_id'], ['user_tests.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_test_id', 'filename')
    )
    op.create_index('ix_user_test_managers_user_test_id', 'user_test_managers', ['user_test_id'], unique=False)
    op.create_table('managers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.Unicode(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dataset_id', 'filename')
    )
    op.create_index('ix_managers_dataset_id', 'managers', ['dataset_id'], unique=False)
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submission_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['submission_id'], ['submissions.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('submission_id')
    )
    op.create_index('ix_tokens_submission_id', 'tokens', ['submission_id'], unique=False)
    op.create_table('user_test_executables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_test_id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_test_id', 'dataset_id'], ['user_test_results.user_test_id', 'user_test_results.dataset_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_test_id'], ['user_tests.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_test_id', 'dataset_id', 'filename')
    )
    op.create_index('ix_user_test_executables_dataset_id', 'user_test_executables', ['dataset_id'], unique=False)
    op.create_index('ix_user_test_executables_user_test_id', 'user_test_executables', ['user_test_id'], unique=False)
    op.create_table('evaluations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submission_id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('testcase_id', sa.Integer(), nullable=False),
    sa.Column('outcome', sa.Unicode(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('execution_time', sa.Float(), nullable=True),
    sa.Column('execution_wall_clock_time', sa.Float(), nullable=True),
    sa.Column('execution_memory', sa.Integer(), nullable=True),
    sa.Column('evaluation_shard', sa.Integer(), nullable=True),
    sa.Column('evaluation_sandbox', sa.Unicode(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['submission_id', 'dataset_id'], ['submission_results.submission_id', 'submission_results.dataset_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['submission_id'], ['submissions.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['testcase_id'], ['testcases.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('submission_id', 'dataset_id', 'testcase_id')
    )
    op.create_index('ix_evaluations_dataset_id', 'evaluations', ['dataset_id'], unique=False)
    op.create_index('ix_evaluations_submission_id', 'evaluations', ['submission_id'], unique=False)
    op.create_index('ix_evaluations_testcase_id', 'evaluations', ['testcase_id'], unique=False)
    op.create_table('social_users',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_level', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('registration_time', sa.DateTime(), nullable=False),
    sa.Column('last_help_time', sa.DateTime(), nullable=False),
    sa.Column('help_count', sa.Integer(), nullable=False),
    sa.Column('institute_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['institute_id'], ['institutes.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('_id', 'id'),
    sa.UniqueConstraint('id')
    )
    op.create_index('ix_social_users_institute_id', 'social_users', ['institute_id'], unique=False)
    op.create_table('executables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submission_id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.Unicode(), nullable=False),
    sa.Column('digest', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['submission_id', 'dataset_id'], ['submission_results.submission_id', 'submission_results.dataset_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['submission_id'], ['submissions.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('submission_id', 'dataset_id', 'filename')
    )
    op.create_index('ix_executables_dataset_id', 'executables', ['dataset_id'], unique=False)
    op.create_index('ix_executables_submission_id', 'executables', ['submission_id'], unique=False)
    op.create_table('task_tags',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['social_tasks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['social_users.id'], ),
    sa.PrimaryKeyConstraint('_id', 'task_id', 'tag_id')
    )
    op.create_table('taskscores',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('time', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['social_users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('_id', 'id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('user_id', 'task_id')
    )
    op.create_index('ix_taskscores_score', 'taskscores', ['score'], unique=False)
    op.create_index('ix_taskscores_task_id', 'taskscores', ['task_id'], unique=False)
    op.create_index('ix_taskscores_user_id', 'taskscores', ['user_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_taskscores_user_id', table_name='taskscores')
    op.drop_index('ix_taskscores_task_id', table_name='taskscores')
    op.drop_index('ix_taskscores_score', table_name='taskscores')
    op.drop_table('taskscores')
    op.drop_table('task_tags')
    op.drop_index('ix_executables_submission_id', table_name='executables')
    op.drop_index('ix_executables_dataset_id', table_name='executables')
    op.drop_table('executables')
    op.drop_index('ix_social_users_institute_id', table_name='social_users')
    op.drop_table('social_users')
    op.drop_index('ix_evaluations_testcase_id', table_name='evaluations')
    op.drop_index('ix_evaluations_submission_id', table_name='evaluations')
    op.drop_index('ix_evaluations_dataset_id', table_name='evaluations')
    op.drop_table('evaluations')
    op.drop_index('ix_user_test_executables_user_test_id', table_name='user_test_executables')
    op.drop_index('ix_user_test_executables_dataset_id', table_name='user_test_executables')
    op.drop_table('user_test_executables')
    op.drop_index('ix_tokens_submission_id', table_name='tokens')
    op.drop_table('tokens')
    op.drop_index('ix_managers_dataset_id', table_name='managers')
    op.drop_table('managers')
    op.drop_index('ix_user_test_managers_user_test_id', table_name='user_test_managers')
    op.drop_table('user_test_managers')
    op.drop_index('ix_institutes_city_id', table_name='institutes')
    op.drop_table('institutes')
    op.drop_index('ix_files_submission_id', table_name='files')
    op.drop_table('files')
    op.drop_index('ix_user_test_files_user_test_id', table_name='user_test_files')
    op.drop_table('user_test_files')
    op.drop_table('user_test_results')
    op.drop_index('ix_testcases_dataset_id', table_name='testcases')
    op.drop_table('testcases')
    op.drop_table('submission_results')
    op.drop_index('ix_printjobs_participation_id', table_name='printjobs')
    op.drop_table('printjobs')
    op.drop_index('ix_user_tests_task_id', table_name='user_tests')
    op.drop_index('ix_user_tests_participation_id', table_name='user_tests')
    op.drop_table('user_tests')
    op.drop_index('ix_submissions_task_id', table_name='submissions')
    op.drop_index('ix_submissions_participation_id', table_name='submissions')
    op.drop_table('submissions')
    op.drop_index('ix_statements_task_id', table_name='statements')
    op.drop_table('statements')
    op.drop_index('ix_questions_participation_id', table_name='questions')
    op.drop_table('questions')
    op.drop_index('ix_messages_participation_id', table_name='messages')
    op.drop_table('messages')
    op.drop_index('ix_submission_format_elements_task_id', table_name='submission_format_elements')
    op.drop_table('submission_format_elements')
    op.drop_index('ix_cities_province_id', table_name='cities')
    op.drop_table('cities')
    op.drop_table('datasets')
    op.drop_table('social_tasks')
    op.drop_index('ix_attachments_task_id', table_name='attachments')
    op.drop_table('attachments')
    op.drop_index('ix_tasks_contest_id', table_name='tasks')
    op.drop_table('tasks')
    op.drop_index('ix_provinces_region_id', table_name='provinces')
    op.drop_table('provinces')
    op.drop_index('ix_participations_user_id', table_name='participations')
    op.drop_index('ix_participations_contest_id', table_name='participations')
    op.drop_table('participations')
    op.drop_index('ix_announcements_contest_id', table_name='announcements')
    op.drop_table('announcements')
    op.drop_table('contests')
    op.drop_table('teams')
    op.drop_table('fsobjects')
    op.drop_table('regions')
    op.drop_table('users')
    op.drop_table('tags')
    ### end Alembic commands ###

    # For some reason, alembic does not generate commands to drop types
    ENUM(name="token_mode").drop(op.get_bind(), checkfirst=False)
    ENUM(name="score_mode").drop(op.get_bind(), checkfirst=False)
